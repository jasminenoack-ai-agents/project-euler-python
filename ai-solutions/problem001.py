"""Project Euler Problem 1 solved by enumerating multiples."""


def solve(limit: int = 1000) -> int:
    """Return the sum of all numbers below ``limit`` that are multiples of 3 or 5."""
    multiples = set()

    # collect multiples of 3
    for n in range(3, limit, 3):
        multiples.add(n)

    # collect multiples of 5
    for n in range(5, limit, 5):
        multiples.add(n)

    return sum(multiples)


if __name__ == "__main__":
    print(solve())
