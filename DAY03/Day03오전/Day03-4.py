class PaymentGateway:
    def process_payment(self, item:str, amount:int) -> str:
        return f'구매품목 : {item} 수량 : {amount}'

class CreditCardGateway(PaymentGateway):
    def process_payment(self, item:str, amount:int) -> str:
            return f'구매품목2 : {item} 수량2 : {amount}'

class BankGateway(PaymentGateway):
    pass

for obj in [CreditCardGateway(), BankGateway()]:
    print(obj.process_payment('식료품',100))



from abc import ABC, abstractmethod
# 부모 class, 내용 없음
class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, item:str, amount:int) -> str:
         pass
# 자식 1 , 내용 있음
class CreditCardGateway(PaymentGateway):
    def process_payment(self, item:str, amount:int) -> str:
            return f'구매품목2 : {item} 수량2 : {amount}'
# 자식 2 , 부모 따라간다고 그대로 상속받음, 근데 부모가 내용이 없어서 None으로 출력
class BankGateway(PaymentGateway):
    pass

obj = BankGateway() # 상속을 받았는데 내용이 없어서 오류가 난다. 
print(obj.process_payment('휴지', 2))
