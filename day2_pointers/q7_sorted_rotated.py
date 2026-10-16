"""
Question: Check if Array is Sorted and Rotated
Task: Verify if an array was originally sorted in non-decreasing order and then rotated some number of times.
"""


def is_sorted_and_rotated(nums):
    """Return whether nums is a rotation of a non-decreasing array."""
    n = len(nums)
    if n < 2:
        return True

    # A rotation has at most one strict drop, including the wraparound pair.
    drops = sum(nums[i] > nums[(i + 1) % n] for i in range(n))
    return drops <= 1


if __name__ == "__main__":
    print(is_sorted_and_rotated([3, 4, 5, 1, 2]))  # True
