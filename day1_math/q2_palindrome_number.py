"""
Question: Palindrome Number
Task: Determine if an integer is a palindrome.
Constraints: Must be solved using pure math operations without converting the integer to a string.
"""


def is_palindrome(number: int) -> bool:
    """Return whether number reads the same forwards and backwards mathematically.

    Time: O(d), where d is the number of digits. Space: O(1).
    """
    if number < 0:
        return False
    if number and number % 10 == 0:
        return False

    remaining = number
    reversed_half = 0
    while remaining > reversed_half:
        reversed_half = reversed_half * 10 + remaining % 10
        remaining //= 10

    # For an odd digit count, discard the middle digit from reversed_half.
    return remaining == reversed_half or remaining == reversed_half // 10
