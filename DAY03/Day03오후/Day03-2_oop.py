"""주문 정보와 계산 기능을 Order 객체로 묶은 리팩터링 예제."""
from dataclasses import dataclass
from decimal import Decimal
from typing import ClassVar


@dataclass(frozen=True)
class Order:
    """주문 생성 시 검증하고, calculate_total()로 정수 금액을 반환합니다.

    회원 유형: 0=일반, 1=5%, 2=10%, 3=20% 할인.
    가격: 0 이상의 유한한 int/float/Decimal. 수량: 1 이상의 정수.
    쿠폰: YES/NO 문자열(대소문자 및 앞뒤 공백 무시) 또는 bool.
    생성 후 가격은 Decimal, 쿠폰은 bool로 저장합니다.
    """
    # 변경: 함수의 인자를 객체 속성으로 옮깁니다.
    # dataclass는 이 속성을 받는 __init__ 메서드를 자동 생성합니다.
    u_type: int
    price: int | float | Decimal
    qty: int
    coupon: str | bool

    # 변경: 모든 주문이 공유하는 계산 정책은 클래스 상수로 관리합니다.
    PAYMENT_PERCENT: ClassVar[tuple[int, ...]] = (100, 95, 90, 80)
    COUPON_AMOUNT: ClassVar[int] = 3000

    def __post_init__(self):
        """자동 생성된 __init__ 직후 입력을 검증하고 정규화합니다."""
        # 변경: 계산할 때가 아니라 주문을 만들 때 잘못된 입력을 거부합니다.
        # bool은 int의 하위 타입이므로 별도로 제외합니다.
        if isinstance(self.u_type, bool) or not isinstance(self.u_type, int):
            raise TypeError("회원 유형은 정수여야 합니다.")
        if self.u_type not in range(len(self.PAYMENT_PERCENT)):
            raise ValueError("회원 유형은 0, 1, 2, 3 중 하나여야 합니다.")
        if isinstance(self.qty, bool) or not isinstance(self.qty, int):
            raise TypeError("수량은 정수여야 합니다.")
        if self.qty <= 0:
            raise ValueError("수량은 1 이상이어야 합니다.")
        price = self._normalize_price(self.price)
        coupon = self._normalize_coupon(self.coupon)
        # frozen=True는 생성 후 속성 변경을 막아 검증된 상태를 유지합니다.
        # 초기 정규화 시에만 object.__setattr__를 사용합니다.
        object.__setattr__(self, "price", price)
        object.__setattr__(self, "coupon", coupon)

    @staticmethod
    def _normalize_price(price: int | float | Decimal) -> Decimal:
        """가격 검증과 변환을 담당하는 내부 보조 메서드입니다."""
        # 변경: 객체 상태가 필요 없는 보조 동작은 정적 메서드로 분리합니다.
        if isinstance(price, bool) or not isinstance(price, (int, float, Decimal)):
            raise TypeError("가격은 int, float 또는 Decimal이어야 합니다.")
        value = Decimal(str(price))
        if not value.is_finite() or value < 0:
            raise ValueError("가격은 0 이상의 유한한 숫자여야 합니다.")
        return value

    @staticmethod
    def _normalize_coupon(coupon: str | bool) -> bool:
        """쿠폰 입력을 bool로 통일합니다."""
        if isinstance(coupon, bool):
            return coupon
        if not isinstance(coupon, str):
            raise TypeError("쿠폰은 YES/NO 문자열 또는 bool이어야 합니다.")
        value = coupon.strip().upper()
        if value not in {"YES", "NO"}:
            raise ValueError("쿠폰 문자열은 YES 또는 NO여야 합니다.")
        return value == "YES"

    def calculate_total(self) -> int:
        """회원 할인 → 쿠폰 차감 → 최소 0원 → 소수 부분 버림."""
        # 변경: 인자를 다시 받지 않고 self에 저장된 주문 정보를 사용합니다.
        # 기존 수정본의 정확한 분수/정수 계산을 유지해 float 오차를 방지합니다.
        numerator, denominator = self.price.as_integer_ratio()
        numerator *= self.qty * self.PAYMENT_PERCENT[self.u_type]
        denominator *= 100
        if self.coupon:
            numerator -= self.COUPON_AMOUNT * denominator
        # 지역 변수만 변경하므로 반복 호출해도 같은 금액을 반환합니다.
        return max(0, numerator) // denominator


if __name__ == "__main__":
    # 변경: 기존 함수 호출 대신 주문 객체 생성 후 메서드를 호출합니다.
    order = Order(u_type=1, price=100, qty=20, coupon="yes")
    print(order.calculate_total())  # 0
    # 각 객체는 독립적인 주문 정보를 가집니다.
    decimal_order = Order(u_type=2, price=1.15, qty=200, coupon="NO")
    print(decimal_order.calculate_total())  # 207
