import sys
from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window, result = deque(), []
        cur_max = float('-inf')

        for i, v in enumerate(nums):
            window.append(v)

            if i < k - 1:
                continue

            if cur_max == float('-inf'):
                cur_max = max(window)
            elif v > cur_max:
                cur_max = v

            result.append(cur_max)

            if cur_max == window.popleft():
                cur_max = float('-inf')

        return result


"""
책에 나온 풀이
"""
