"""
https://leetcode.com/problems/product-of-array-except-self/
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return self.inplace(nums)

    def maintain_left_right_product_for_each_item(self, nums: List[int]) -> List[int]:
        l = len(nums)
        left_products = [1 for _ in range(l)]
        right_products = [1 for _ in range(l)]
        products = [1 for _ in range(l)]
        left_product = 1
        right_product = 1
        for i in range(1, l):
            left_product *= nums[i - 1]
            left_products[i] = left_product
        for i in range(l - 2, -1, -1):
            right_product *= nums[i + 1]
            right_products[i] = right_product
        for i in range(l):
            products[i] = left_products[i] * right_products[i]
        return products

    def inplace(self, nums: List[int]) -> List[int]:
        l = len(nums)
        products = [1 for _ in range(l)]
        left_product = 1
        for i in range(1, l):
            left_product *= nums[i - 1]
            products[i] = left_product
        right_product = 1
        for i in range(l - 2, -1, -1):
            right_product *= nums[i + 1]
            products[i] *= right_product
        return products


if __name__ == "__main__":
    print([24, 12, 8, 6] == Solution().productExceptSelf([1, 2, 3, 4]))
