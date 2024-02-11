"""
https://leetcode.com/problems/rotate-array/
"""

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int, solution=1) -> None:
        k %= len(nums)
        if k == len(nums):
            return
        if solution == 1:
            self.solution_rotate_all_then_part(nums, k)

    def solution_rotate_all_then_part(self, nums: List[int], k: int) -> None:
        self.rotate_all(nums, 0, len(nums) - 1)
        self.rotate_all(nums, 0, k - 1)
        self.rotate_all(nums, k, len(nums) - 1)

    def rotate_all(self, nums: List[int], start: int, end: int) -> None:
        i = start
        j = end
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 10
    answer = [5, 6, 7, 1, 2, 3, 4]
    Solution().rotate(nums, k)
    print(nums == answer)
