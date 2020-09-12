from typing import List
import functools


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        res = []
        for i in range(len(nums)):
            res.append(p)
            p *= nums[i]
        p = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= p
            p *= nums[i]

        return res

# 다시 풀것!!