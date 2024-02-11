"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums1 = nums.copy()
        yellow = set()
        red = set()
        k = 0
        for num in nums1:
            if num in red:
                continue
            if num in yellow:
                yellow.remove(num)
                red.add(num)
                nums[k] = num
                k += 1
            else:
                yellow.add(num)
                nums[k] = num
                k += 1
        return k


if __name__ == "__main__":
    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    answer = [0, 0, 1, 1, 2, 3, 3]
    k = Solution().removeDuplicates(nums)
    print(k == len(answer))  # print(True)
    print(nums[:k] == answer)  # print(True)
