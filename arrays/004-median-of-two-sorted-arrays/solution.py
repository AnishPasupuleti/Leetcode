# Problem: https://leetcode.com/problems/median-of-two-sorted-arrays/
# Difficulty: Hard
# Tags: Array, Sorting

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1 + nums2
        nums3.sort()
        n = len(nums3)

        if n % 2 == 0:
            mid = n // 2
            return (nums3[mid - 1] + nums3[mid]) / 2
        else:
            mid = n // 2
            return nums3[mid]
