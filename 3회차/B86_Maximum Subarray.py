from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [nums[0]]
        res = nums[0]

        for i, num in enumerate(nums[1:], 1):
            dp.append(max(num, num + dp[-1]))
            res = max(res, dp[-1])

        return res


print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))