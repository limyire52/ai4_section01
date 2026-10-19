from main import analyze_fizzbuzz


def test_analyze_fizzbuzz():
    cases = [
        (-10, {"FizzBuzz": 0, "Fizz": 0, "Buzz": 0, "Number": 0}),
        (0, {"FizzBuzz": 0, "Fizz": 0, "Buzz": 0, "Number": 0}),
        (1, {"FizzBuzz": 0, "Fizz": 0, "Buzz": 0, "Number": 1}),
        (3, {"FizzBuzz": 0, "Fizz": 1, "Buzz": 0, "Number": 2}),
        (5, {"FizzBuzz": 0, "Fizz": 1, "Buzz": 1, "Number": 3}),
        (15, {"FizzBuzz": 1, "Fizz": 4, "Buzz": 2, "Number": 8}),
        (16, {"FizzBuzz": 1, "Fizz": 4, "Buzz": 2, "Number": 9}),
        (30, {"FizzBuzz": 2, "Fizz": 8, "Buzz": 4, "Number": 16}),
    ]

    for limit, expected in cases:
        actual = analyze_fizzbuzz(limit)
        assert actual == expected, f"limit={limit}: {actual} != {expected}"
        assert sum(actual.values()) == max(limit, 0)
        print(f"PASS limit={limit}: {actual}")


if __name__ == "__main__":
    test_analyze_fizzbuzz()
    print("All 8 test cases passed.")
