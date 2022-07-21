from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)

        nums[2] += nums[0]
        res = max(nums[2], nums[1])

        for i in range(3, len(nums)):
            nums[i] += max(nums[i - 3], nums[i - 2])
            res = max(res, nums[i])

        return res


print(Solution().rob([2,7,9,3,1]))