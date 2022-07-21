from typing import List
import sys


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [nums[0]]

        res = nums[0]
        min_val = min(0, nums[0])
        for i in range(1, len(nums)):
            dp.append(dp[-1] + nums[i])
            res = max(res, dp[i] - min_val)
            min_val = min(min_val, dp[i])

        return res


print(Solution().maxSubArray([-2,1]))