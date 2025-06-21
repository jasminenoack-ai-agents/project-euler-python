"""Solution to Project Euler Problem 5 (AI generated)."""


def solve(limit: int = 20) -> int:
    """Return the smallest positive number evenly divisible by all numbers from
    1 to ``limit``.

    2520 is the smallest number that can be divided by each of the numbers from
    1 to 10 without any remainder. What is the smallest positive number that is
    evenly divisible by all of the numbers from 1 to 20?

    This implementation computes the least common multiple (LCM) of the range
    ``[1, limit]``.
    """
    from math import gcd

    lcm = 1
    for n in range(2, limit + 1):
        lcm = lcm * n // gcd(lcm, n)
    return lcm


if __name__ == "__main__":
    print(solve())
