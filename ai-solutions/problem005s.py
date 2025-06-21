"""Functional solution to Project Euler Problem 5."""

from functools import reduce
from math import gcd


def solve(limit: int = 20) -> int:
    """Return the smallest positive number evenly divisible by all numbers from
    1 to ``limit`` using a functional approach without loops.
    """
    return reduce(lambda lcm, n: lcm * n // gcd(lcm, n), range(2, limit + 1), 1)


if __name__ == "__main__":
    print(solve())
