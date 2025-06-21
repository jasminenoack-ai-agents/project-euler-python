"""AI-generated alternative solution to Project Euler Problem 3.

This version avoids the use of the ``//`` and ``%`` operators.
"""

from typing import Tuple


def _divmod_no_division(dividend: int, divisor: int) -> Tuple[int, int]:
    """Return the quotient and remainder of ``dividend`` / ``divisor``.

    The implementation uses subtraction and bit shifting instead of the
    ``//`` and ``%`` operators.
    """
    if divisor == 0:
        raise ZeroDivisionError("division by zero")
    quotient = 0
    remainder = dividend
    while remainder >= divisor:
        multiple = 1
        value = divisor
        # Increase ``value`` to the highest power of two multiple
        # that does not exceed ``remainder``.
        while value <= (remainder >> 1):
            value <<= 1
            multiple <<= 1
        remainder -= value
        quotient += multiple
    return quotient, remainder


def solve(number: int = 600851475143) -> int:
    """Return the largest prime factor of ``number`` without using ``//`` or ``%``."""
    n = number
    factor = 2
    last_factor = 1
    while factor * factor <= n:
        q, r = _divmod_no_division(n, factor)
        if r == 0:
            last_factor = factor
            n = q
            q, r = _divmod_no_division(n, factor)
            while r == 0:
                n = q
                q, r = _divmod_no_division(n, factor)
        factor += 1 if factor == 2 else 2
    if n > 1:
        last_factor = n
    return last_factor


if __name__ == "__main__":
    print(solve())
