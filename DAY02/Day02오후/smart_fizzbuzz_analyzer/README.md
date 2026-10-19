# Mission 1: Smart FizzBuzz Analyzer

## 문제정의
1부터 limit까지의 정수를 순회하며 각 숫자를 FizzBuzz, Fizz, Buzz, Number 중 하나로 분류하고, 각 분류의 개수를 계산한다.

## 입력값
- 함수: `analyze_fizzbuzz(limit: int) -> dict`
- `limit`: 순회 범위의 마지막 정수. 범위에 limit도 포함한다.
- 프로그램을 직접 실행하면 정수 하나를 입력받는다.

## 출력값
다음 네 키를 갖고, 값이 정수인 딕셔너리를 반환한다.

```python
{"FizzBuzz": int, "Fizz": int, "Buzz": int, "Number": int}
```

예를 들어 limit가 15이면 다음을 반환한다.

```python
{"FizzBuzz": 1, "Fizz": 4, "Buzz": 2, "Number": 8}
```

## 제약조건
1. for문으로 1부터 limit까지 순회한다.
2. 3과 5의 공배수이면 FizzBuzz만 증가시킨다.
3. 그 외의 3의 배수이면 Fizz만 증가시킨다.
4. 그 외의 5의 배수이면 Buzz만 증가시킨다.
5. 나머지 숫자는 Number만 증가시킨다.
6. if/elif/else를 사용하여 숫자 하나가 정확히 한 분류에만 포함되게 한다.
7. limit가 1 미만이면 모든 카운트가 0인 딕셔너리를 반환한다.
8. 입력은 정수라고 가정하며, 최대 입력 크기는 별도로 지정되지 않았다.

## 테스트 및 실행
`assert`는 함수가 아니라 조건이 참인지 검사하는 파이썬 문장이다. 거짓이면 AssertionError가 발생한다.

`test_main.py`에서 음수, 0, 1, 3, 5, 15, 16, 30을 검증한다. 각 기대 결과와 실제 결과를 비교하고, 모든 카운트의 합이 순회한 숫자의 개수와 같은지도 확인한다.

이 폴더에서 다음 명령어로 실행한다.

```text
python main.py
python test_main.py
```
