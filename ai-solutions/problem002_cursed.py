"""AI-generated 'cursed' variant solution to Project Euler Problem 2.

This version sums even Fibonacci numbers up to ``limit`` but only
includes numbers whose digit sum in base 7 is prime.
"""

from __future__ import annotations


def _digit_sum_base7(n: int) -> int:
    """Return the sum of digits of ``n`` when represented in base 7."""
    total = 0
    while n:
        total += n % 7
        n //= 7
    return total


def _is_prime(n: int) -> bool:
    """Return ``True`` if ``n`` is a prime number."""
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def solve(limit: int = 4_000_000) -> int:
    """Return the modified Fibonacci sum up to ``limit``."""
    total = 0
    a, b = 1, 2
    while a <= limit:
        if a % 2 == 0 and _is_prime(_digit_sum_base7(a)):
            total += a
        a, b = b, a + b
    return total


if __name__ == "__main__":
    print(solve())
