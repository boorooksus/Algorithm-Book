from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        d = [0 for _ in range(len(nums))]
        d[0] = nums[0]
        for i in range(1, len(nums)):
            d[i] = d[i - 1] + nums[i]
            ans = max(ans, d[i])
            for j in range(i):
                ans = max(ans, d[i] - d[j])
        return ans

print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

"""
leetcode: 53
시간초과
"""