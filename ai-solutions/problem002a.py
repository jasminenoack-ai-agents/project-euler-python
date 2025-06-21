"""AI solution to Project Euler Problem 2 using tail recursion."""


def solve(limit: int = 4_000_000) -> int:
    """Return the sum of even Fibonacci numbers up to ``limit`` using tail recursion."""

    def _helper(a: int, b: int, total: int) -> int:
        if a > limit:
            return total
        if a % 2 == 0:
            total += a
        return _helper(b, a + b, total)

    return _helper(1, 2, 0)


if __name__ == "__main__":
    print(solve())
