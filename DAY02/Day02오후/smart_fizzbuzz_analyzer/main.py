def analyze_fizzbuzz(limit: int) -> dict:
    """1부터 limit까지의 숫자를 네 종류로 분류해 개수를 반환한다."""
    counts = {"FizzBuzz": 0, "Fizz": 0, "Buzz": 0, "Number": 0}

    if limit < 1:
        return counts

    for number in range(1, limit + 1):
        if number % 3 == 0 and number % 5 == 0:
            counts["FizzBuzz"] += 1
        elif number % 3 == 0:
            counts["Fizz"] += 1
        elif number % 5 == 0:
            counts["Buzz"] += 1
        else:
            counts["Number"] += 1

    return counts


if __name__ == "__main__":
    limit = int(input("limit: "))
    print(analyze_fizzbuzz(limit))
