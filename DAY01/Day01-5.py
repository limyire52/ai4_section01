# 숫자 맞추기 게임
# 규칙
# 컴퓨터가 1~100사이의 값을 임의로 생성한 후 
# 사용자가 맞추는 게임
# 사용자가 입력한 값이 크면 크고, 작으면 작다라고 알려줌

# -- 필요한 기능
# 입력: int(input())
# 컴퓨터가 1~100사이의 임의의 숫자를 선택
# import random   #랜덤으로 가져온다. import는 내장이 되어있음. / install은 다운로드해서 새로 가져오는 것

# for i in range(3) : # 3번 반복해서 랜덤으로 가져옴
#     number = random.randint(1,100)  #random 안에 있는 randint
#     print(number)
# 비교연산자를 통해 크다 작다 판별
# 순환문, 조건문, break

# import random

# com_number = random.randint(1, 100)

# while True: 
#     user_number = int(input("1~100 : "))

#     if user_number < com_number: 
#         print("컴퓨터보다 작습니다.")

#     elif user_number > com_number:    # elif user_number > com_number: 가능
#         print("컴퓨터보다 큽니다.")

#     else:   # else:  가능
#         print("정답입니다.")
#         break

# 맞출 때 까지 반복

#맥시멈을 넣고 싶으면 for문으로 반복문 사용해야함

#몇번만에 성공했는지 나타내기 위해 count 함수 추가
import random

com_number = random.randint(1, 100)
count = 0
while True: 
    user_number = int(input("1~100 : "))
    count += 1  # += 은 복합연산대입자, 자기자신에 계속 더하기 1씩 계속 더해짐
# 다른 프로그래밍 언어에서는 ++로 쓰기도 함

    if user_number < com_number: 
        print("컴퓨터보다 작습니다.")

    elif user_number > com_number:    # elif user_number > com_number: 가능
        print("컴퓨터보다 큽니다.")

    else:   # else:  가능
        print(f"정답입니다. 총 시도횟수는 {count}회 입니다.")   # f는 문자열 안에 변수의 값을 넣을 수 있도록 해줌, 중괄호를 넣어 숫자를 문자열에 넣어줌
        break
