def calculate_even_sum_and_count(n):
    """Return the sum and count of even integers from 1 through n."""
    even_sum = 0
    even_count = 0

    if n < 1:
        return {"Sum": 0, "Count": 0}

    for i in range(1, n + 1):
        if i % 2 == 0:
            even_sum += i
            even_count += 1

    return {"Sum": even_sum, "Count": even_count}


if __name__ == "__main__":
    n = int(input("n: "))
    print(calculate_even_sum_and_count(n))
