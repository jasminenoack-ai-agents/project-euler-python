"""Matrix-based alternative solution for Project Euler Problem 3."""

from __future__ import annotations

import numpy as np
from math import gcd


def _matrix_step(x: int, n: int) -> int:
    """Return ``(x*x + 1) % n`` using a matrix product."""
    mat = np.array([[x, 1], [0, 1]], dtype=object)
    vec = np.array([x, 1], dtype=object)
    return int((mat @ vec)[0] % n)


def _pollards_rho(n: int) -> int:
    """Return a non-trivial factor of ``n`` using Pollard's rho."""
    if n % 2 == 0:
        return 2
    x = 2
    y = 2
    d = 1
    while d == 1:
        x = _matrix_step(x, n)
        y = _matrix_step(_matrix_step(y, n), n)
        d = gcd(abs(x - y), n)
    return d


def _is_prime(n: int) -> bool:
    """Return ``True`` if ``n`` is prime."""
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    p = 3
    while p * p <= n:
        if n % p == 0:
            return False
        p += 2
    return True


def solve(number: int = 600851475143) -> int:
    """Return the largest prime factor of ``number`` using matrix multiplication."""

    def factorize(n: int) -> list[int]:
        if n == 1:
            return []
        if _is_prime(n):
            return [n]
        d = n
        while d == n:
            d = _pollards_rho(n)
        return factorize(d) + factorize(n // d)

    return max(factorize(number))


if __name__ == "__main__":
    print(solve())
