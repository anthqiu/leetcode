"""
https://leetcode.com/problems/candy/
"""

from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        if len(ratings) == 1:
            return 1
        # find each increase/decrease sequence
        current_level = 1
        min_level = 1
        current_segment_length = 1
        current_segment_candies = 1
        num_candies = 0
        current_direction = ratings[1] - ratings[0]
        print(current_level, " init")
        for idx in range(1, len(ratings)):
            delta = ratings[idx] - ratings[idx - 1]
            if current_direction > 0 and delta > 0:
                current_segment_length += 1
                current_level += 1
                current_segment_candies += current_level
                print(current_level, " +")
            elif current_direction < 0 and delta < 0:
                current_segment_length += 1
                current_level -= 1
                min_level = min(min_level, current_level)
                current_segment_candies += current_level
                print(current_level, " <")
            elif current_direction == 0 and delta == 0:
                if idx < len(ratings) - 1 and ratings[idx + 1] != ratings[idx]:
                    additional_candies_per_child = 1 - min_level
                    additional_candies = additional_candies_per_child * current_segment_length
                    current_segment_candies += additional_candies
                    num_candies += current_segment_candies
                    current_direction = ratings[idx + 1] - ratings[idx]
                    current_segment_length = 1
                    current_segment_candies = 1
                    current_level = 1
                    min_level = 1
                    print(current_level, " *0 ", num_candies)
                else:
                    current_segment_length += 1
                    current_segment_candies += current_level
                    print(current_level, " =")
            else:
                additional_candies_per_child = 1 - min_level
                additional_candies = additional_candies_per_child * current_segment_length
                current_segment_candies += additional_candies
                num_candies += current_segment_candies
                if delta == 0 and idx < len(ratings) - 1 and ratings[idx + 1] != ratings[idx]:
                    delta = ratings[idx + 1] - ratings[idx]
                current_direction = delta
                current_segment_length = 1
                current_level = 1 if delta <= 0 else 2
                min_level = current_level
                current_segment_candies = current_level
                print(current_level, " * ", num_candies)
        additional_candies_per_child = max(0, 1 - min_level)
        additional_candies = additional_candies_per_child * current_segment_length
        current_segment_candies += additional_candies
        num_candies += current_segment_candies
        print(num_candies)
        return num_candies


if __name__ == '__main__':
    ratings = [1, 3, 4, 5, 2]
    print(11 == Solution().candy(ratings))
    ratings = [1, 2, 2, 2, 1]
    print(7 == Solution().candy(ratings))
    ratings = [1, 0, 2]
    print(5 == Solution().candy(ratings))
    ratings = [1, 3, 2, 2, 1]
    print(7 == Solution().candy(ratings))
