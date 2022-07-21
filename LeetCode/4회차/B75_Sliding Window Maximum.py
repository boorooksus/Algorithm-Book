from typing import List
from collections import deque
import sys


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        cur_max = float('-inf')
        window = deque()
        for i in range(len(nums)):
            window.append(nums[i])

            if i < k - 1:
                continue

            if cur_max == float('-inf'):
                cur_max = max(window)
            elif nums[i] > cur_max:
                cur_max = nums[i]

            res.append(cur_max)

            if cur_max == window.popleft():
                cur_max = float('-inf')

        return res


print(Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7]
,3))