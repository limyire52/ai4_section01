# 1 사용자로 부터 데이터를 입력받아서(5개) 리스트에 저장하고
# 2 저장된 리스트의 값 중에서 짝수만 출력해보기

#number1 = int(input("첫번째 숫자를 입력하세요 : "))
#number2 = int(input("두번째 숫자를 입력하세요 : "))
#number3 = int(input("세번째 숫자를 입력하세요 : "))
#number4 = int(input("네번째 숫자를 입력하세요 : "))
#number5 = int(input("다섯번째 숫자를 입력하세요 : "))
# 1 을 풀면 이렇게 풀 수 있음, 하지만 데이터 양이 많을 때 좋지 못함, 함수를 사용!

#for i in range(5) : #변수 i는 용도가 없다.
    #int(input("숫자를 입력하세요 : "))

#for i in range(5) : #변수 i는 용도가 없다.
    #int(input(f"{i+1} : 숫자를 입력하세요 : "))

#for i in range(5) : #변수 i는 용도가 없다.
   #print(f"{i+1} : 숫자를 입력하세요 : ")   f는 포맷

scores = [] #scores 라는 리스트
for i in range(5) :
    score = int(input(f"{i+1} : 숫자를 입력하세요 : ")) # score 데이터를 사용자에게 받기
    scores.append(score)    # scores 라는 리스트에 입력된 score 추가

print('리스트변수의 값 :', scores)  # 입력된 리스트 출력

for i in scores:    # scores 안에 있는 것들을 순환해서 반복할 것 (아래있는 조건문 만족시)
    if i % 2 == 0 : # 2로 나누었을 때 나누어 떨어지는 것
       print(i)