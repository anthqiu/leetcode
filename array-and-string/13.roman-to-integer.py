"""
https://leetcode.com/problems/roman-to-integer/
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        l = len(s)
        current_digit = 0
        result = 0
        for i in range(l - 1, -1, -1):
            if s[i] == 'I':
                if current_digit == 0:
                    result += 1
                else:
                    result -= 1
            elif s[i] == 'V':
                current_digit = 1
                result += 5
            elif s[i] == 'X':
                if current_digit <= 1:
                    result += 10
                    current_digit = 1
                else:
                    result -= 10
            elif s[i] == 'L':
                current_digit = 2
                result += 50
            elif s[i] == 'C':
                if current_digit <= 2:
                    result += 100
                    current_digit = 2
                else:
                    result -= 100
            elif s[i] == 'D':
                current_digit = 3
                result += 500
            elif s[i] == 'M':
                if current_digit <= 3:
                    result += 1000
                    current_digit = 3
                else:
                    result -= 1000
        return result

if __name__ == '__main__':
    print(1994 == Solution().romanToInt("MCMXCIV"))