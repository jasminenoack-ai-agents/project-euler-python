"""AI-generated solution to Project Euler Problem 4."""

def _is_palindrome(number: int) -> bool:
    """Return ``True`` if ``number`` reads the same forwards and backwards."""
    s = str(number)
    return s == s[::-1]


def solve(digits: int = 3) -> int:
    """Return the largest palindrome made from the product of two ``digits``-digit numbers."""
    if digits < 1:
        raise ValueError("digits must be >= 1")

    lower = 10 ** (digits - 1)
    upper = 10 ** digits - 1
    best = 0

    for i in range(upper, lower - 1, -1):
        for j in range(i, lower - 1, -1):
            product = i * j
            if product <= best:
                break
            if _is_palindrome(product):
                best = product
                break
    return best


if __name__ == "__main__":
    print(solve())
