from typing import List
from collections import deque

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ans = [0 for _ in range(len(T))]
        stack = []
        for i, cur in enumerate(T):
            # 현재 온도가 스택보다 높다면 정답 처리
            while stack and cur > T[stack[-1]]:
                last = stack.pop()
                ans[last] = i - last
            stack.append(i)
        return ans

# leetcode 739
#
