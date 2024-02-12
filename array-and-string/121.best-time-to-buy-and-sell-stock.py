"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_value = 1e4 + 1
        max_profit = 0
        for price in prices:
            if price < min_value:
                min_value = price
            max_profit = max(max_profit, price - min_value)
        return max_profit


if __name__ == '__main__':
    prices_1 = [7, 1, 5, 3, 6, 4]
    print(Solution().maxProfit(prices_1) == 5)
    prices_2 = [7, 6, 4, 3, 1]
    print(Solution().maxProfit(prices_2) == 0)
    prices_3 = [7]
    print(Solution().maxProfit(prices_3) == 0)
