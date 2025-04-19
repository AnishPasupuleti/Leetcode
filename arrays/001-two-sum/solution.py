# Problem: https://leetcode.com/problems/two-sum/
# Difficulty: Easy
# Tags: Array, Hash Map

class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i
