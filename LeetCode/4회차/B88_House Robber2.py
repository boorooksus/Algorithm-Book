from typing import List
from sys import setrecursionlimit
setrecursionlimit(10 ** 9)


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]

        dp = [-1 for _ in range(len(nums))]
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        def _rob(idx: int) -> int:
            if idx < 0:
                return 0
            if dp[idx] != -1:
                return dp[idx]

            dp[idx] = max(_rob(idx - 1), _rob(idx - 2) + nums[idx])
            return dp[idx]

        return _rob(len(nums) - 1)
