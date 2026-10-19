import random


def practice_5():
    """
    실습 5. 숫자 맞추기 게임 (Day01-5.py)
    목표: 난수, 조건문, 반복문을 조합해 게임을 만든다.
    문제:
    1. 컴퓨터가 1~100 중 정수 하나를 선택하게 하세요.
    2. 사용자가 숫자를 입력할 때마다 시도 횟수를 1 증가시키세요.
    3. 입력이 정답보다 작거나 큰지 알려 주세요.
    4. 정답을 맞히면 시도 횟수를 출력하고 반복을 종료하세요.
    복습: randint(1, 100)은 양 끝값을 포함합니다.
          while True는 계속 반복하며, break가 반복문을 종료합니다.
          count += 1은 count = count + 1과 같습니다. count는 변수입니다.
    확인 방법: 50부터 입력하고 안내에 따라 범위를 좁혀 정답을 찾아보세요.
    추가 도전: 최대 7회로 제한하거나, 1~100 범위 밖 입력을 처리하세요.
               횟수 제한은 for 또는 while의 조건으로 구현할 수 있습니다.
    """
    com_number = random.randint(1, 100)
    count = 0

    while True:
        user_number = int(input("1~100 사이의 숫자를 입력하세요: "))
        count += 1

        if user_number < com_number:
            print("입력한 숫자가 정답보다 작습니다.")
        elif user_number > com_number:
            print("입력한 숫자가 정답보다 큽니다.")
        else:
            print(f"정답입니다. 총 시도 횟수는 {count}회입니다.")
            break
