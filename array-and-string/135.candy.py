"""
https://leetcode.com/problems/candy/
"""

from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        if len(ratings) == 1:
            return 1
        candies = self.init_candies(ratings)
        n = len(ratings)
        for i in range(n):
            self.optimize_candies(ratings, candies, i, n, False)
        for i in range(n):
            self.optimize_candies(ratings, candies, n - 1 - i, n, True)
        cnt = 0
        for i in candies:
            cnt += i
        return cnt

    def init_candies(self, ratings: List[int]) -> List[int]:
        candies = [0 for i in range(len(ratings))]
        current_candies = 1
        candies[0] = 1
        min_candies = 1

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                current_candies += 1
                candies[i] = current_candies
            else:
                current_candies -= 1
                candies[i] = current_candies
                min_candies = min(current_candies, min_candies)

        increase = 1 - min_candies

        for i in range(len(ratings)):
            candies[i] += increase

        return candies

    def optimize_candies(self, ratings: List[int], candies: List[int], idx: int, n: int, right: bool) -> None:
        has_left = idx != 0
        has_right = idx != n - 1
        left_larger = True if not has_left else ratings[idx - 1] >= ratings[idx]
        right_larger = True if not has_right else ratings[idx + 1] >= ratings[idx]
        if left_larger and right_larger:
            candies[idx] = 1
            return
        left_min = -1
        if has_left:
            if left_larger:
                left_min = candies[idx - 1] - 1  # 0 if left_equal else 1
            else:
                left_min = candies[idx - 1] + 1
        right_min = -1
        if has_right:
            if right_larger:
                right_min = candies[idx + 1] - 1  # if right_equal else 1
            else:
                right_min = candies[idx + 1] + 1
        if left_larger:
            candies[idx] = right_min
        elif right_larger:
            candies[idx] = left_min
        else:
            candies[idx] = max(left_min, right_min)


if __name__ == '__main__':
    print(11 == Solution().candy([1, 3, 4, 5, 2]))
    print(7 == Solution().candy([1, 2, 2, 2, 1]))
    print(5 == Solution().candy([1, 0, 2]))
    print(7 == Solution().candy([1, 3, 2, 2, 1]))
    print(9 == Solution().candy([1, 2, 4, 4, 3]))
    print(13 == Solution().candy([1, 2, 87, 87, 87, 2, 1]))
