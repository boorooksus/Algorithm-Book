from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)

        dp = [nums[0], max(nums[0], nums[1])]

        for i, num in enumerate(nums[2:], 2):
            dp.append(max(dp[i - 1], dp[i - 2] + num))

        return dp[-1]


print(Solution().rob([2,1,1,2]))
