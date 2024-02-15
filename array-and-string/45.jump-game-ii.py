"""
https://leetcode.com/problems/jump-game-ii/
"""

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        current_jump_times = 0
        last_possible_furthest = 0
        current_possible_furthest = -1
        i = 0
        while i < len(nums) - 1:
            current_possible_furthest = max(i + nums[i], current_possible_furthest)
            if i == last_possible_furthest:
                print(i)
                # we cannot go any further, so we increase jump cnt
                current_jump_times += 1
                last_possible_furthest = current_possible_furthest
            i += 1
        print(current_jump_times)
        return current_jump_times


if __name__ == "__main__":
    print(2 == Solution().jump([2, 3, 1, 1, 4]))
