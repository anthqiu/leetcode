"""
https://leetcode.com/problems/longest-common-prefix/
"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lens = [len(s) for s in strs]
        l = len(strs)

        for accu in range(1, lens[0] + 1):
            c = strs[0][accu - 1]
            for i in range(1, l):
                if lens[i] < accu:
                    return strs[0][:accu - 1]
                if strs[i][accu - 1] != c:
                    return strs[0][:accu - 1]

        return strs[0]


if __name__ == "__main__":
    print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
