from typing import List

"""
Top LeetCode Problems:
✅ LC 303 - Range Sum Query - Immutable (Easy)
✅ LC 560 - Subarray Sum Equals K (Medium)
✅ LC 1248 - Count Number of Nice Subarrays (Medium)
✅ LC 1732 - Find the Highest Altitude (Easy)
✅ LC 238 - Product of Array Except Self (Medium)
"""
class PrefixSum:
    def __init__(self, nums: List[int]):
        """Build prefix sum array"""
        self.prefix = [0]
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    def rangeSum(self, left: int, right: int) -> int:
        """Get sum of nums[left:right+1]"""
        return self.prefix[right + 1] - self.prefix[left]


def subarraySum(nums: List[int], k: int) -> int:
    """Count subarrays with sum == k"""
    count = 0
    sum_freq = {0: 1}  # prefix_sum -> frequency
    current_sum = 0

    for num in nums:
        current_sum += num
        # Check if (current_sum - k) exists
        if current_sum - k in sum_freq:
            count += sum_freq[current_sum - k]
        sum_freq[current_sum] = sum_freq.get(current_sum, 0) + 1

    return count

if __name__ == "__main__":
    cont = subarraySum([2, 7, 11, 7, 15], 7)
    print(cont)