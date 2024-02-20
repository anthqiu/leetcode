"""
https://leetcode.com/problems/h-index/
"""

from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        i = 0
        while i < len(citations):
            if i + 1 <= citations[i]:
                i += 1
                continue
            else:
                break
        return i
