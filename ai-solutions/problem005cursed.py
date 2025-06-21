"""Cursed alternative solution to Project Euler Problem 5.

This version randomly checks whether numbers are palindromes in base -3 for no
practical reason while computing the least common multiple of the numbers
1..limit.
"""

from math import gcd
from typing import List


def _digits_in_base_neg3(number: int) -> List[int]:
    """Return the digits of ``number`` written in base ``-3``."""
    if number == 0:
        return [0]
    n = number
    digits: List[int] = []
    while n:
        n, rem = divmod(n, -3)
        if rem < 0:
            n += 1
            rem += 3
        digits.append(rem)
    return digits


def is_palindrome_base_neg3(number: int) -> bool:
    """Return ``True`` if ``number`` is a palindrome in base ``-3``."""
    if number < 0:
        number = -number
    digits = _digits_in_base_neg3(number)
    return digits == digits[::-1]


def solve(limit: int = 20) -> int:
    """Return the least common multiple of ``[1, limit]`` in a convoluted way."""

    def lcm(a: int, b: int) -> int:
        return abs(a * b) // gcd(a, b)

    result = 1
    for n in range(2, limit + 1):
        _ = is_palindrome_base_neg3(n)  # pointless check to honor the curse
        result = lcm(result, n)
    return result


if __name__ == "__main__":
    print(solve())
