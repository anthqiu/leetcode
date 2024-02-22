"""
https://leetcode.com/problems/gas-station/
"""

from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        l = len(gas)
        delta = [gas[i] - cost[i] for i in range(l)]
        accu = 0
        min_accu = 0
        min_accu_i = 0

        for i in range(l):
            accu += delta[i]
            if accu < min_accu:
                min_accu = accu
                min_accu_i = i + 1

        if accu >= 0:
            return min_accu_i % l

        return -1
