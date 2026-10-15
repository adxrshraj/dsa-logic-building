"""
Question: Fast Exponentiation
Task: Compute x^n in O(log n) time complexity.
Constraints: Handle negative powers and edge cases like exponent 0.
"""


def fast_power(base: float, exponent: int) -> float:
    """Compute base**exponent by exponentiation by squaring.

    Time: O(log |exponent|). Space: O(1). A zero base with a negative
    exponent raises ZeroDivisionError, as it does for ordinary division.
    """
    if exponent == 0:
        return 1

    power = abs(exponent)
    result = 1
    factor = base
    while power:
        if power % 2 == 1:
            result *= factor
        factor *= factor
        power //= 2

    if exponent < 0:
        return 1 / result
    return result
