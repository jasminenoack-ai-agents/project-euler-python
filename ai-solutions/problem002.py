"""AI solution to Project Euler Problem 2."""


def solve(limit: int = 4_000_000) -> int:
    """Return the sum of even Fibonacci numbers up to ``limit``.

    Starting with 1 and 2, generate Fibonacci numbers not exceeding
    ``limit`` and sum the values that are even.
    """
    total = 0
    a, b = 1, 2

    while a <= limit:
        if a % 2 == 0:
            total += a
        a, b = b, a + b

    return total


if __name__ == "__main__":
    print(solve())
