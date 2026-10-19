# 딕셔너리
# key-value 한쌍이 하나의 값

# 리스트 vs 딕셔너리
# 리스트: 데이터를 담음, 대괄호 안에 데이터는 단일요소
# 딕셔너리: 데이터를 담음, key:value 형태로 작성 - key는 유일무이한 것, 절대로 중복될 수 없음 (ex.주민번호)

list_1 = [10,20,30,[1,2,3]]
dict_1 = { 'kor': 80 , 'eng' : 80 , 'math' : 90}

# dict_1.keys()     # 가장 중요 ! key이기 때문
# dict_1.values()   
# dict_1.items()    

for i in dict_1: # key 값만 가져온다. = for i in dict_1.keys() 
    print(i)
# kor eng math
for i in dict_1.values():
    print(i)
# 80 80 90
for i in dict_1.items():
    print(i)
# ('kor', 80) ('eng', 80) ('math', 90)

for i in dict_1.items():
    print(i, i[0], i[1])
#('kor', 80) kor 80 ('eng', 80) eng 80  ('math', 90) math 90 
# -> for니까 순환, 한번씩 돌아가면서 i가 됨, 따라서 첫번째 i는 ('kor',80) 여기서 i[0]은 kor i[1]은 80 /순환/ 다음 i는 ('eng', 80) ...

for key, value in dict_1.items():
    print(f"key={key} value={value}")

