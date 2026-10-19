"""주문 금액 계산 수정본. 원본 Day03-2.py는 변경하지 않습니다."""

from decimal import Decimal


# 수정: 회원별 결제 비율과 쿠폰 금액을 이름 있는 상수로 관리합니다.
PAYMENT_PERCENT = {0: 100, 1: 95, 2: 90, 3: 80}
COUPON_AMOUNT = 3000


def calc_order_legacy(u_type, price, qty, coupon):
    """회원 할인 → 쿠폰 차감 → 최소 0원 → 소수 부분 버림 순으로 계산합니다.

    기존 호출과의 호환을 위해 함수 이름과 인자 순서를 유지합니다.
    u_type: 0(일반), 1(5% 할인), 2(10% 할인), 3(20% 할인).
    price: 0 이상의 유한한 int, float 또는 Decimal 단가.
    qty: 1 이상의 정수 수량. bool은 허용하지 않습니다.
    coupon: YES/NO 문자열(대소문자와 앞뒤 공백 무시) 또는 bool.
    반환값은 정수 금액이며, 잘못된 입력은 TypeError/ValueError로 알립니다.
    """
    # 수정: bool은 int의 하위 타입이므로 정수 검증에서 명시적으로 제외합니다.
    if isinstance(u_type, bool) or not isinstance(u_type, int):
        raise TypeError("회원 유형은 정수여야 합니다.")
    if u_type not in PAYMENT_PERCENT:
        raise ValueError("회원 유형은 0, 1, 2, 3 중 하나여야 합니다.")

    if isinstance(qty, bool) or not isinstance(qty, int):
        raise TypeError("수량은 정수여야 합니다.")
    if qty <= 0:
        raise ValueError("수량은 1 이상이어야 합니다.")

    # 수정: 음수, 숫자 문자열, NaN, 무한대를 계산 전에 거부합니다.
    if isinstance(price, bool) or not isinstance(price, (int, float, Decimal)):
        raise TypeError("가격은 int, float 또는 Decimal이어야 합니다.")
    decimal_price = Decimal(str(price))
    if not decimal_price.is_finite() or decimal_price < 0:
        raise ValueError("가격은 0 이상의 유한한 숫자여야 합니다.")

    # 수정: 'yes', ' YES '도 쿠폰으로 인식하고, 오타는 조용히 무시하지 않습니다.
    if isinstance(coupon, bool):
        use_coupon = coupon
    elif isinstance(coupon, str):
        normalized_coupon = coupon.strip().upper()
        if normalized_coupon not in {"YES", "NO"}:
            raise ValueError("쿠폰 문자열은 YES 또는 NO여야 합니다.")
        use_coupon = normalized_coupon == "YES"
    else:
        raise TypeError("쿠폰은 YES/NO 문자열 또는 bool이어야 합니다.")

    # 수정: 가격을 정확한 분수로 바꿔 정수 연산합니다.
    # 예: 1.15 × 200 × 90%가 206.999...로 계산되는 float 오차를 방지합니다.
    numerator, denominator = decimal_price.as_integer_ratio()
    numerator *= qty * PAYMENT_PERCENT[u_type]
    denominator *= 100

    if use_coupon:
        numerator -= COUPON_AMOUNT * denominator

    # 수정: 반올림하지 않고 기존 정책대로 최종 금액의 소수 부분만 버립니다.
    return max(0, numerator) // denominator


# 수정: 다른 모듈에서 가져올 때 예제 계산과 출력이 실행되지 않도록 합니다.
if __name__ == "__main__":
    result = calc_order_legacy(1, 100, 20, "yes")
    print(result)  # 예상 결과: 0 (회원 할인 후 쿠폰을 차감하고 최소 0원 적용)
