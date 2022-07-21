from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def get_max(idx):
            if idx in d:
                return d[idx]
            d[idx] = max(get_max(idx - 1), get_max(idx - 2) + nums[idx])
            return d[idx]
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        d = dict()
        d[0] = nums[0]
        d[1] = max(nums[0], nums[1])

        return get_max(len(nums) - 1)

print(Solution().rob([0,0]))

"""
leetcode: 198
다이나믹 프로그래밍
"""