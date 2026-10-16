"""
Question: Reverse an Array / Subarray In-Place
Task: Reverse an array or a specific subarray range using two converging pointers (left, right).
"""


def reverse_range(nums, left=0, right=None):
    """Reverse nums[left:right+1] in place and return nums.

    Bounds are inclusive. Empty arrays and ranges with left >= right are no-ops.
    """
    if right is None:
        right = len(nums) - 1
    if left < 0 or right >= len(nums):
        raise IndexError("range is outside the array")

    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    return nums


if __name__ == "__main__":
    values = [1, 2, 3, 4, 5]
    reverse_range(values, 1, 3)
    print(values)  # [1, 4, 3, 2, 5]
