"""점수 전처리: 입력 검증, 예외 원인 보존, 자동 처리 리포트.

원본의 결함과 수정 방향
1. data/row의 형태를 검증하지 않아 TypeError의 발생 위치가 불명확했다.
2. score 누락, None, 빈 문자열, 숫자 변환 실패를 구별하지 않았다.
3. float(True)는 1.0이고 NaN/무한대도 float 변환에 성공한다.
4. 음수/100 초과도 정규화했다. 이 파일은 0~100점이라는 정책을 가정한다.
5. 한 행의 실패로 전체가 중단되며 행 위치와 처리 실적을 알 수 없었다.
6. 변환 예외에 업무 맥락이 없었다. raise ... from ...으로 원인을 보존한다.

기본은 즉시 중단(raise), on_error='skip'은 실패 행을 기록하고 계속한다.
성공률의 분모는 실제 검증을 시도한 행 수다. 중단 후 미처리 행은 제외한다.
입력 전체를 미리 리스트로 만들지 않아 생성기와 대용량 입력도 처리한다.
원본 입력을 변경하지 않으며, 반올림은 원본처럼 round(..., 4)를 사용한다.
이는 이진 부동소수점 및 Python의 동률 짝수 반올림 정책을 따른다.
"""

from __future__ import annotations

import math
import sys
from collections.abc import Iterable, Mapping
from dataclasses import dataclass, field
from decimal import Decimal
from numbers import Real
from typing import Literal, TextIO


class RowValidationError(ValueError):
    """1부터 시작하는 행 번호와 기계 판독 가능한 오류 코드를 보존한다."""

    def __init__(self, row_number: int, code: str, reason: str):
        self.row_number = row_number
        self.code = code
        super().__init__(f"{row_number}행 [{code}]: {reason}")


class DataIterationError(RuntimeError):
    """입력 생성기 자체가 실패한 경우. 행 검증 실패와 구분한다."""


@dataclass(frozen=True)
class ValidationIssue:
    row_number: int
    code: str
    message: str


@dataclass
class ProcessingReport:
    attempted: int = 0
    succeeded: int = 0
    issues: list[ValidationIssue] = field(default_factory=list)
    completed: bool = False
    iteration_failed: bool = False

    @property
    def failed(self) -> int:
        return len(self.issues)

    @property
    def success_rate(self) -> float | None:
        # 빈 입력을 100% 성공으로 오인하지 않도록 비율을 정의하지 않는다.
        return self.succeeded / self.attempted if self.attempted else None

    def format(self) -> str:
        rate = "N/A (처리 행 없음)" if self.success_rate is None else f"{self.success_rate:.2%}"
        status = "완료" if self.completed else "중단 (미처리 행 수 미집계)"
        iteration = ", 입력 순회 오류 있음" if self.iteration_failed else ""
        return (
            f"[전처리 리포트] {status}{iteration} | 시도 {self.attempted}행, "
            f"성공 {self.succeeded}행, 검증 실패 {self.failed}행 | 성공률 {rate}"
        )


@dataclass
class PreprocessResult:
    # skip 모드에서는 실패 행이 빠진다. 원본 위치는 row_numbers로 확인한다.
    values: list[float]
    row_numbers: list[int]
    report: ProcessingReport


def _validate_data(data: object) -> Iterable[object]:
    """문자열과 단일 사전이 행의 목록으로 오인되는 것을 막는다."""
    if isinstance(data, (str, bytes, bytearray, Mapping)) or not isinstance(data, Iterable):
        raise TypeError("data는 사전 형태의 행들을 담은 iterable이어야 합니다.")
    return data


def _validate_score(row: object, row_number: int) -> float:
    """행/키/자료형/숫자/유한성/범위 검증을 한 곳에 캡슐화한다."""
    if not isinstance(row, Mapping):
        raise RowValidationError(row_number, "row_type", "행은 Mapping이어야 합니다.")
    try:
        raw_score = row["score"]
    except KeyError as exc:
        raise RowValidationError(row_number, "missing_score", "score 키가 없습니다.") from exc

    if raw_score is None:
        raise RowValidationError(row_number, "null_score", "score가 None입니다.")
    # bool은 int의 하위 타입이므로 숫자 타입 검사보다 먼저 거부해야 한다.
    if isinstance(raw_score, bool) or not isinstance(raw_score, (str, Real, Decimal)):
        raise RowValidationError(row_number, "score_type", "score는 실수 또는 숫자 문자열이어야 합니다.")
    if isinstance(raw_score, str) and not raw_score.strip():
        raise RowValidationError(row_number, "empty_score", "score가 빈 문자열입니다.")
    try:
        score = float(raw_score)
    except (TypeError, ValueError, OverflowError) as exc:
        # 원래 예외는 __cause__에 남고, 새 예외는 발생 행과 업무 맥락을 제공한다.
        raise RowValidationError(row_number, "score_conversion", "score를 실수로 변환할 수 없습니다.") from exc
    if not math.isfinite(score):
        raise RowValidationError(row_number, "non_finite", "NaN과 무한대는 허용하지 않습니다.")
    if not 0.0 <= score <= 100.0:
        raise RowValidationError(row_number, "out_of_range", "score는 0~100 범위여야 합니다.")
    return score


def preprocess(
    data: Iterable[object],
    *,
    on_error: Literal["raise", "skip"] = "raise",
    emit_report: bool = True,
    report_stream: TextIO | None = None,
) -> PreprocessResult:
    """정규화 값, 원본 행 번호, 상세 리포트를 반환한다.

    raise 모드에서 실패하면 예외가 전파되고 부분 결과는 반환하지 않는다.
    skip 모드는 RowValidationError만 건너뛴다. 코드 버그나 생성기 오류를
    정상적인 데이터 오류로 삼키지 않는다. 원본 점수는 로그에 출력하지 않는다.
    잘못된 호출 인수는 처리를 시작하기 전에 거부하므로 리포트 대상이 아니다.
    """
    if on_error not in ("raise", "skip"):
        raise ValueError("on_error는 'raise' 또는 'skip'이어야 합니다.")
    if not isinstance(emit_report, bool):
        raise TypeError("emit_report는 bool이어야 합니다.")
    rows = _validate_data(data)
    stream = sys.stderr if report_stream is None else report_stream
    if emit_report and not callable(getattr(stream, "write", None)):
        raise TypeError("report_stream은 write()를 제공해야 합니다.")
    report = ProcessingReport()
    result = PreprocessResult(values=[], row_numbers=[], report=report)
    try:
        try:
            iterator = iter(rows)
        except Exception as exc:
            report.iteration_failed = True
            raise DataIterationError("입력 순회를 시작하지 못했습니다.") from exc
        while True:
            try:
                row = next(iterator)
            except StopIteration:
                report.completed = True
                break
            except Exception as exc:
                # next() 경계에서만 포착한다. skip이어도 입력 순회 실패는 중단한다.
                report.iteration_failed = True
                raise DataIterationError(f"{report.attempted + 1}행을 읽던 중 입력 순회에 실패했습니다.") from exc
            report.attempted += 1
            try:
                score = _validate_score(row, report.attempted)
            except RowValidationError as exc:
                report.issues.append(ValidationIssue(exc.row_number, exc.code, str(exc)))
                if on_error == "raise":
                    raise  # 같은 예외와 원래 traceback을 그대로 전파한다.
                continue
            result.values.append(round(score / 100.0, 4))
            result.row_numbers.append(report.attempted)
            report.succeeded += 1
    finally:
        # 성공/검증 실패/입력 순회 실패 모두 자동 집계한다.
        if emit_report:
            active_error = sys.exc_info()[1]
            try:
                print(report.format(), file=stream)
            except Exception as report_error:
                # 출력 실패가 원래 처리 예외를 덮지 않게 한다.
                # 정상 처리 중 출력 실패라면 호출자에게 그대로 알린다.
                if active_error is None:
                    raise
                if hasattr(active_error, "add_note"):
                    active_error.add_note(f"리포트 출력도 실패했습니다: {type(report_error).__name__}")
    return result


def preprocess_legacy(data: Iterable[object], **kwargs: object) -> list[float]:
    """기존 함수 이름과 list 반환 형태를 유지하는 호환 진입점."""
    return preprocess(data, **kwargs).values


if __name__ == "__main__":
    sample = [{"score": "85"}, {"score": "잘못된 값"}, {"score": 100}, {"score": True}]
    demo = preprocess(sample, on_error="skip")
    print("정규화 결과:", demo.values)
    print("원본 행 번호:", demo.row_numbers)
    for issue in demo.report.issues:
        print(issue.message)
