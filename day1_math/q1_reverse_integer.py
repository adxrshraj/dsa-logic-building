"""
Question: Reverse an Integer
Task: Reverse an integer mathematically using modulo (% 10) and floor division (// 10).
Constraints: Handle negative values and 32-bit signed integer overflow conditions.
Do not use string conversions (e.g., str[::-1]).
"""


def reverse_integer(number: int) -> int:
    """Reverse decimal digits, returning 0 if the result exceeds signed 32-bit range.

    Time: O(d), where d is the number of digits. Space: O(1).
    """
    lower_bound = -(2**31)
    upper_bound = 2**31 - 1
    sign = -1 if number < 0 else 1
    remaining = abs(number)
    reversed_number = 0

    while remaining:
        digit = remaining % 10
        remaining //= 10
        reversed_number = reversed_number * 10 + digit

    reversed_number *= sign
    if reversed_number < lower_bound or reversed_number > upper_bound:
        return 0
    return reversed_number
