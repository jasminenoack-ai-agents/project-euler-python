"""Alternative solution to Project Euler Problem 4 for palindromes in base 7."""


def _is_palindrome_in_base(number: int, base: int) -> bool:
    """Return ``True`` if ``number`` is a palindrome when written in ``base``."""
    if base < 2:
        raise ValueError("base must be >= 2")
    if number < 0:
        return False
    digits = []
    n = number
    while n:
        digits.append(n % base)
        n //= base
    if not digits:
        digits.append(0)
    return digits == digits[::-1]


def solve(digits: int = 3, base: int = 7) -> int:
    """Return the largest product of two ``digits``-digit numbers that is a
    palindrome in ``base``."""
    if digits < 1:
        raise ValueError("digits must be >= 1")
    if base < 2:
        raise ValueError("base must be >= 2")

    lower = 10 ** (digits - 1)
    upper = 10 ** digits - 1
    best = 0

    for i in range(upper, lower - 1, -1):
        for j in range(i, lower - 1, -1):
            product = i * j
            if product <= best:
                break
            if _is_palindrome_in_base(product, base):
                best = product
                break
    return best


if __name__ == "__main__":
    print(solve())
