"""
https://leetcode.com/problems/merge-sorted-array/
"""

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums11 = nums1[:m]
        i = 0
        j = 0
        for k in range(m + n):
            if i >= m:
                nums1[k] = nums2[j]
                j += 1
                continue
            if j >= n:
                nums1[k] = nums11[i]
                i += 1
                continue
            if nums11[i] < nums2[j]:
                nums1[k] = nums11[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1


if __name__ == "__main__":
    import random

    m = random.randint(100, 1000)
    n = random.randint(100, 1000)
    nums1 = sorted([random.randint(1, 1000) for i in range(m)])
    nums11 = nums1 + [0 for i in range(n)]
    nums2 = sorted([random.randint(1, 1000) for i in range(n)])

    Solution().merge(nums11, m, nums2, n)

    print(nums11 == sorted(nums1 + nums2))  # print(True)
