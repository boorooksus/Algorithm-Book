from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        s = []
        ans = [0 for _ in range(len(T))]
        for i, v in enumerate(T):
            while s and s[-1][1] < v:
                idx, val = s[-1]
                del s[-1]
                ans[idx] = i - idx
            s.append((i, v))
        return ans
