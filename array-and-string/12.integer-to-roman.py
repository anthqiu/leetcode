"""
https://leetcode.com/problems/integer-to-roman/
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        symbols = [('M', 1000), ("CM", 900), ('D', 500), ("CD", 400),
                   ('C', 100), ("XC", 90), ('L', 50), ("XL", 40),
                   ('X', 10), ("IX", 9), ('V', 5), ('IV', 4), ('I', 1)]
        output = ""
        for symbol, value in symbols:
            while num >= value:
                output += symbol
                num -= value
        return output


if __name__ == "__main__":
    print("MCMXCIV" == Solution().intToRoman(1994))
