"""
Question: Count Digits & Digit Sum
Task: Calculate the total count of digits and the sum of all digits in a given integer iteratively.
"""


def count_digits_and_sum(number: int) -> tuple[int, int]:
    """Return (digit count, digit sum), ignoring a leading minus sign.

    Time: O(d), where d is the number of digits. Space: O(1).
    """
    remaining = abs(number)
    if remaining == 0:
        return 1, 0

    count = 0
    digit_sum = 0
    while remaining:
        digit_sum += remaining % 10
        count += 1
        remaining //= 10
    return count, digit_sum
