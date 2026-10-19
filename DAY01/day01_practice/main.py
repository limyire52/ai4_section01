"""이 파일을 실행하면 실습 선택 메뉴가 열립니다."""

if __package__:
    from .exercises.variables import practice_1
    from .exercises.conditions import practice_2
    from .exercises.lists import practice_3
    from .exercises.multiplication import practice_4
    from .exercises.number_game import practice_5
else:
    from day01_practice.exercises.variables import practice_1
    from day01_practice.exercises.conditions import practice_2
    from day01_practice.exercises.lists import practice_3
    from day01_practice.exercises.multiplication import practice_4
    from day01_practice.exercises.number_game import practice_5


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
