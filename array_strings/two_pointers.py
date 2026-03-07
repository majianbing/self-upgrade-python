from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    """Find two numbers that sum to target in SORTED array"""
    left, right = 0, len(nums) - 1

    while left < right:
        total = nums[left] + nums[right]

        if total == target:
            return [left, right]
        elif total < target:
            left += 1
        else:
            right -= 1

    return []


def removeDuplicates(nums: List[int]) -> int:
    """Remove duplicates in-place"""
    if len(nums) == 0:
        return 0

    left = 0
    for right in range(1, len(nums)):
        if nums[right] != nums[left]:
            left += 1
            nums[left] = nums[right]

    return left + 1

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(twoSum(nums, target))
    nums = [0, 0, 1, 1,4]
    print(removeDuplicates(nums))