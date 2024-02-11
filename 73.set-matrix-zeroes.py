"""
https://leetcode.com/problems/set-matrix-zeroes/
"""

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zero_rows = set()
        zero_cols = set()
        n_row = len(matrix)
        n_col = len(matrix[0])
        for row in range(n_row):
            for col in range(n_col):
                if matrix[row][col] == 0:
                    zero_rows.add(row)
                    zero_cols.add(col)
        for z_row in zero_rows:
            for i in range(n_col):
                matrix[z_row][i] = 0
        for z_col in zero_cols:
            for i in range(n_row):
                matrix[i][z_col] = 0


if __name__ == "__main__":
    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    answer = [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
    Solution().setZeroes(matrix)
    print(matrix == answer)  # print(True)
