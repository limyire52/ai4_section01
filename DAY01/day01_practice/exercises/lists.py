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
