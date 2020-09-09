from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        p = 1
        for i in range(len(nums)):
            out.append(p)
            p *= nums[i]

        p = 1
        for i in range(len(nums) - 1, -1, -1):
            out[i] *= p
            p *= nums[i]
        return out

# leetcode: 238
# 나눗셈을 이용하지 않고 O(N)으로 풀이