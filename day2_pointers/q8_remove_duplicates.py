"""
Question: Remove Duplicates from Sorted Array
Task: Modify a sorted array in-place such that each unique element appears only once.
Constraints: Return the new length; use O(1) extra space.
"""


def remove_duplicates(nums):
    """Deduplicate sorted nums in place and return its unique-prefix length."""
    if not nums:
        return 0

    write = 1
    for read in range(1, len(nums)):
        if nums[read] != nums[write - 1]:
            nums[write] = nums[read]
            write += 1
    return write


if __name__ == "__main__":
    values = [1, 1, 2, 2, 3]
    length = remove_duplicates(values)
    print(values[:length])  # [1, 2, 3]
