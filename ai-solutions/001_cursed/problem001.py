"""AI solution to variant of Project Euler Problem 1 with word-palindrome filter."""

from typing import Dict


_units: Dict[int, str] = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}

_teens: Dict[int, str] = {
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
}

_tens: Dict[int, str] = {
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
}


def _number_to_words(n: int) -> str:
    """Return the English words for ``n`` (0 <= ``n`` < 1000)."""
    if n == 0:
        return _units[0]

    words = []
    if n >= 100:
        words.append(f"{_units[n // 100]} hundred")
        n %= 100
        if n == 0:
            return " ".join(words)
    if n >= 20:
        tens_val = (n // 10) * 10
        word = _tens[tens_val]
        n %= 10
        if n > 0:
            word += f"-{_units[n]}"
        words.append(word)
    elif n >= 10:
        words.append(_teens[n])
    elif n > 0:
        words.append(_units[n])
    return " ".join(words)


def _is_palindrome_word(word: str) -> bool:
    """Return ``True`` if ``word`` is a palindrome when ignoring spaces and hyphens."""
    cleaned = word.replace(" ", "").replace("-", "").lower()
    return cleaned == cleaned[::-1]


def solve(limit: int = 1000) -> int:
    """Sum numbers below ``limit`` divisible by 3 or 5 whose English word is a palindrome."""
    total = 0
    for n in range(1, limit):
        if n % 3 == 0 or n % 5 == 0:
            word = _number_to_words(n)
            if _is_palindrome_word(word):
                total += n
    return total


if __name__ == "__main__":
    print(solve())
