from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque()
        res = []
        cur_max = -20000

        for i, v in enumerate(nums):
            window.append(v)
            if i < k:
                continue

            if cur_max == -20000:
                cur_max = max(window)
            elif cur_max < window[-1]:
                cur_max = window[-1]

            res.append(cur_max)
            if window.popleft() == cur_max:
                cur_max = -20000

        return res

sol = Solution()
print(sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))

"""
leetcode: 239
뭐야 왜 해답도 시간초과야
"""