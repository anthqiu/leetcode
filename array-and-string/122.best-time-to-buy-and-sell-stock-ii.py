"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        holding = False
        inf = 1e4 + 1
        current_min = inf
        profit = 0
        for day in range(len(prices) - 1):
            if not holding and prices[day] < prices[day + 1]:
                holding = True
                current_min = prices[day]
            if holding and prices[day] > prices[day + 1]:
                holding = False
                profit += prices[day] - current_min
                current_min = inf
        if holding:
            profit += prices[-1] - current_min
        return profit


if __name__ == "__main__":
    prices_1 = [7, 1, 5, 3, 6, 4]
    print(7 == Solution().maxProfit(prices_1))
    prices_2 = [1, 2, 3, 4, 5]
    print(4 == Solution().maxProfit(prices_2))
