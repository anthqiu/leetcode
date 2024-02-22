"""
https://leetcode.com/problems/length-of-last-word/
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        accu = 0
        while s[i] == " " and i >= 0:
            i -= 1
        while s[i] != " " and i >= 0:
            accu += 1
            i -= 1
        return accu


if __name__ == "__main__":
    print(4 == Solution().lengthOfLastWord("   fly me   to   the moon  "))
