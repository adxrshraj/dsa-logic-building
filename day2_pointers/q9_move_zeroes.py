"""
Question: Move Zeroes
Task: Shift all zeroes in an array to the end while maintaining the relative order of non-zero elements.
Constraints: Must be done in-place without copying the array.
"""


def move_zeroes(nums):
    """Move zeroes to the end in place, preserving non-zero order."""
    write = 0
    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write], nums[read] = nums[read], nums[write]
            write += 1


if __name__ == "__main__":
    values = [0, 1, 0, 3, 12]
    move_zeroes(values)
    print(values)  # [1, 3, 12, 0, 0]
