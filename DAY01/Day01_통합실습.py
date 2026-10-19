"""
Python 기초 통합 실습
====================
원본: Day01-1.py ~ Day01-5.py

사용 방법
1. 이 파일을 Python으로 실행합니다.
2. 메뉴에서 1~5를 선택해 실습합니다. 0을 입력하면 종료합니다.
3. 다시 풀 때는 각 함수의 문제를 읽고 구현 부분을 직접 작성해 보세요.
   아래 코드는 실행 가능한 정답 예시입니다.

학습 순서
변수와 연산 → 입력과 조건문 → 리스트와 반복문 → 중첩 반복문 → 숫자 게임
외부 패키지 설치는 필요하지 않습니다. random은 Python 표준 라이브러리입니다.
"""

import random


def practice_1():
    """
    실습 1. 변수와 덧셈 (Day01-1.py)
    목표: 변수에 정수를 저장하고 계산 결과를 출력한다.
    문제: number1에 100, number2에 200을 저장하고 두 값의 합을 출력하세요.
    예상 결과: number1 + number2 = 300
    복습: =는 값 대입, +는 덧셈, print()는 출력입니다.
    추가 도전: 두 값을 바꾸고 뺄셈, 곱셈, 나눗셈 결과도 출력하세요.
    """
    number1 = 100
    number2 = 200
    print("number1 + number2 =", number1 + number2)


def practice_2():
    """
    실습 2. 입력과 조건문 (Day01-2.py)
    목표: 입력받은 숫자에 따라 다른 메시지를 출력한다.
    문제: 점수를 입력받아 60점 이상이면 '합격', 그 외에는 '불합격'을 출력하세요.
    확인 입력: 59 → 불합격 / 60 → 합격 / 100 → 합격
    복습: input()의 결과는 문자열이므로 int()로 정수로 변환합니다.
          >=는 이상 비교이며, if/else의 실행 범위는 들여쓰기로 구분합니다.
    추가 도전: 0~100 범위를 벗어나면 '잘못된 점수입니다.'를 출력하세요.
    """
    score = int(input("점수를 입력하세요: "))
    if score >= 60:
        print("합격")
    else:
        print("불합격")


def practice_3():
    """
    실습 3. 리스트와 짝수 찾기 (Day01-3.py)
    목표: 여러 값을 리스트에 저장하고 조건에 맞는 값만 출력한다.
    문제: 정수 5개를 입력받아 리스트에 저장하고, 리스트와 짝수를 출력하세요.
    확인 입력: 1, 2, 3, 4, 5 → 리스트 [1, 2, 3, 4, 5], 짝수 2와 4
    복습: []는 빈 리스트, append()는 값 추가, range(5)는 0~4입니다.
          %는 나머지 연산이며, 정수를 2로 나눈 나머지가 0이면 짝수입니다.
          f"{i + 1}"은 계산 결과를 문자열에 넣습니다.
    추가 도전: 홀수만 출력하거나 입력받을 숫자의 개수를 사용자가 정하게 하세요.
    """
    scores = []
    for i in range(5):
        score = int(input(f"{i + 1}번째 숫자를 입력하세요: "))
        scores.append(score)

    print("리스트변수의 값:", scores)
    print("짝수:")
    for number in scores:
        if number % 2 == 0:
            print(number)


def practice_4():
    """
    실습 4. 중첩 반복문과 구구단 (Day01-4.py)
    목표: 반복문 안에 반복문을 넣어 구구단을 표 형태로 출력한다.
    문제: 2~9단을 가로로 나란히 출력하고, 각 단의 곱하는 수는 1~9로 하세요.
    첫 번째 줄: 2 x 1 = 2 ... 9 x 1 = 9
    두 번째 줄: 2 x 2 = 4 ... 9 x 2 = 18
    복습: range(2, 10)은 2~9입니다. 끝값 10은 포함하지 않습니다.
          바깥 반복문은 행, 안쪽 반복문은 같은 행의 각 단을 담당합니다.
          end="\t"는 출력 후 줄바꿈 대신 탭을 붙입니다.
          print()는 다음 행으로 줄바꿈합니다.
    추가 도전: 반복문 순서를 바꾸어 2단 전체, 3단 전체 순서로 출력하세요.
    """
    for multiplier in range(1, 10):
        for dan in range(2, 10):
            print(f"{dan} x {multiplier} = {dan * multiplier}", end="\t")
        print()


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


def main():
    # 함수는 관련 코드를 이름으로 묶은 것입니다.
    # 이 파일에서는 실습을 골라 실행하고 다시 실행하기 위해 함수를 사용합니다.
    practices = {
        "1": practice_1,
        "2": practice_2,
        "3": practice_3,
        "4": practice_4,
        "5": practice_5,
    }

    while True:
        print("\n=== Python 기초 통합 실습 ===")
        print("1. 변수와 덧셈")
        print("2. 입력과 합격 판정")
        print("3. 리스트와 짝수 찾기")
        print("4. 중첩 반복문과 구구단")
        print("5. 숫자 맞추기 게임")
        print("0. 종료")
        choice = input("실습 번호를 선택하세요: ").strip()

        if choice == "0":
            print("실습을 종료합니다.")
            break
        if choice not in practices:
            print("0~5 중에서 선택하세요.")
            continue

        practice = practices[choice]
        print(practice.__doc__)
        try:
            practice()
        except ValueError:
            # int()로 바꿀 수 없는 입력을 받으면 안내 후 메뉴로 돌아갑니다.
            print("정수를 입력해야 합니다. 메뉴에서 실습을 다시 선택하세요.")


if __name__ == "__main__":
    main()
