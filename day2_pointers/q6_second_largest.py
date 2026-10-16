"""
Question: Find Second Largest Element
Task: Find the second distinct largest element in an array.
Constraints: Must run in O(N) time and O(1) auxiliary space.
"""


def second_largest(nums):
    """Return the second distinct largest value, or None if it doesn't exist."""
    largest = second = None

    for value in nums:
        if largest is None or value > largest:
            second = largest
            largest = value
        elif value != largest and (second is None or value > second):
            second = value

    return second


if __name__ == "__main__":
    print(second_largest([12, 35, 1, 10, 34, 1]))  # 34
