"""
https://leetcode.com/problems/jump-game/
"""

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        len_nums = len(nums)
        rightest = 0
        for i in range(len_nums):
            if i > rightest:
                return False
            rightest = max(rightest, i + nums[i])
        return True


if __name__ == "__main__":
    print(True == Solution().canJump([2, 3, 1, 1, 4]))
    print(False == Solution().canJump([3, 2, 1, 0, 4]))
    print(True == Solution().canJump([0]))
