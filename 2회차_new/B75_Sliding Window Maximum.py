from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        res = []
        window = deque()
        cur_max = float('-inf')

        for i, num in enumerate(nums):
            window.append(num)
            if i < k - 1:
                continue

            if cur_max == float('-inf'):
                cur_max = max(window)

            elif num > cur_max:
                cur_max = num

            res.append(cur_max)

            if window.popleft() == cur_max:
                cur_max = float('-inf')

        return res


# print(Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
print(Solution().maxSlidingWindow([9, 11], 2))
