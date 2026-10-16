"""
Question: Rotate Array by K Positions
Task: Rotate an array to the right by k steps.
Constraints: Implement using the optimal array-reversal algorithm with O(1) space.
"""


def rotate_right(nums, k):
    """Rotate nums right by k steps in place using O(1) extra space."""
    n = len(nums)
    if n == 0:
        return nums
    k %= n

    def reverse(left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)
    return nums


if __name__ == "__main__":
    values = [1, 2, 3, 4, 5, 6, 7]
    rotate_right(values, 3)
    print(values)  # [5, 6, 7, 1, 2, 3, 4]
