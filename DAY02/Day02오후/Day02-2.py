# zip
list_1 = ['a', 'b', 'c']
list_2 = [100,200,300]
result = zip(list_1, list_2)

# zip을 생성한 객체를 dictionary 변환
result = dict(result)
print(result)

# zip은 임시로 두개를 쌍으로 묶는 집합형태를 나타낸다. 
# list(zip()) -> 리스트로 집을 묶으면 데이터가 된다. 

# 제로샷: 출력결과, 기대값 기대 없음
# 원샷: 예시를 하나 줌
# 투샷: 예시를 여러개 줌