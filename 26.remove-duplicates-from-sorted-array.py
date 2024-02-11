"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums1 = nums.copy()
        k = 0
        for i in range(len(nums1) - 1):
            if nums1[i] != nums1[i + 1]:
                nums[k] = nums[i]
                k += 1
        nums[k] = nums1[len(nums1) - 1]
        k += 1
        return k


if __name__ == '__main__':
    import random

    m = 1000
    nums = sorted([random.randint(1, 100) for i in range(m)])
    nums_set = sorted(list(set(nums)))
    k = Solution().removeDuplicates(nums)
    print(k == len(nums_set))  # print(True)
    print(nums[:k] == nums_set)  # print(True)
