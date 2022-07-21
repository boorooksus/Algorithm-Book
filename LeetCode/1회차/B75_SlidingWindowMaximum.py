from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        end = k - 1
        dq = deque()

        for i in range(k):
            dq.append(nums[i])
        cur_max = max(dq)
        res = [cur_max]

        while end < len(nums) - 1:
            end += 1

            last = dq.popleft()
            dq.append(nums[end])

            if last == cur_max:
                cur_max = max(dq)
            elif nums[end] > cur_max:
                cur_max = nums[end]

            res.append(cur_max)

        return res

sol = Solution()
print(sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))

"""
leetcode: 239
시간초과
"""