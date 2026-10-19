# import random
# ages = random.sample(range(15,100),10)  #나이=15세부터 99세까지의 집합 중 랜덤으로 10개 고름 (사용자는 모름)
# results = []
# for i in ages:
#     if i >=20:
#         results.append('성인')
#     else:
#         results.append('미성년자')

# print(results)


#리스트에서 불량을 모두 지우고 정상만 남게

items = ['정상','불량','불량','정상']
# for item in items :
#     if item == '불량' :
#         items.remove('불량')

# print(f'검수결과: {items}')

# items = ['정상','불량','불량','정상']
# for item in items[:] :  # [:]의 역할 : 
#     if item == '불량' :
#         items.remove('불량')

# print(f'검수결과: {items}')

result = [item for item in items if item != '불량'] #삭제에 초점이 아니라 불량을 뺀 나머지를 출력하도록 한다.
# 결과 = 아이템에 있는 애들 중 아이템에 불량이 아니면 result에 item을 붙여준다  

print(f'검수결과 : {result}')