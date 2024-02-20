"""
https://leetcode.com/problems/h-index/
"""

from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        l = len(citations)
        for i in range(l):
            if citations[l - 1 - i] >= l - i:
                return l - i
        return 0
