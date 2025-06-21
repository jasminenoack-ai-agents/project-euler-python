"""AI-generated solution to Project Euler Problem 3."""


def solve(number: int = 600851475143) -> int:
    """Return the largest prime factor of ``number``."""
    n = number
    factor = 2
    last_factor = 1
    while factor * factor <= n:
        if n % factor == 0:
            last_factor = factor
            n //= factor
            while n % factor == 0:
                n //= factor
        factor += 1 if factor == 2 else 2
    if n > 1:
        last_factor = n
    return last_factor


if __name__ == "__main__":
    print(solve())
