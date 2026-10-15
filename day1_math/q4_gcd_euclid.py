"""
Question: Greatest Common Divisor (Euclid’s Algorithm)
Task: Implement the GCD algorithm using both iterative and recursive approaches.
"""


def gcd_iterative(a: int, b: int) -> int:
    """Return the non-negative GCD using Euclid's iterative algorithm.

    Time: O(log(min(|a|, |b|))) for nonzero inputs. Space: O(1).
    """
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def gcd_recursive(a: int, b: int) -> int:
    """Return the non-negative GCD using Euclid's recursive algorithm.

    Time: O(log(min(|a|, |b|))) for nonzero inputs. Space: O(log(min(|a|, |b|)))
    call-stack frames; gcd(0, 0) returns 0.
    """
    a, b = abs(a), abs(b)
    if b == 0:
        return a
    return gcd_recursive(b, a % b)
