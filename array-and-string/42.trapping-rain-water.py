"""
https://leetcode.com/problems/trapping-rain-water/
"""

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        l = len(height)
        left_highest = [0 for _ in range(l)]
        right_highest = [0 for _ in range(l)]
        left = 0
        right = 0
        for i in range(1, l):
            left = max(left, height[i - 1])
            left_highest[i] = left
        for i in range(l-2, -1, -1):
            right = max(right, height[i+1])
            right_highest[i] = right
        total = 0
        for i in range(l):
            water_height = min(left_highest[i], right_highest[i])
            trapped = max(water_height - height[i], 0)
            total += trapped
        return total
