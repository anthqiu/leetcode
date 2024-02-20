"""
https://leetcode.com/problems/h-index/
"""

from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l = len(citations)

        # count #papers that got #citations. indices are #citations, values are #papers with #citations
        cit_freq = [0 for i in range(l + 1)]
        for c in citations:
            # if paper got #citations more than len(citations), count as len(citations)
            if c >= l:
                cit_freq[l] += 1
            else:
                cit_freq[c] += 1
        cnt = 0
        for i in range(l):
            # (l - i) is #papers, cnt is #papers with #citations greater or equal than (l - i)
            cnt += cit_freq[l - i]
            if cnt >= l - i:
                # if #papers with [#citations greater than (l - i)] is greater than or equal to (l - i), then return
                return l - i
        return 0
