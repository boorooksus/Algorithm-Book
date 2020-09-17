from typing import List

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = []
        for i, v in enumerate(T):
            cnt, j = 0, i + 1
            if j < len(T) and v < T[j]:
                res.append(1)
                continue
            while j < len(T) and v >= T[j]:
                cnt += 1
                j += 1
            if cnt > 0:
                cnt += 1
            if cnt > len(T) - i - 1:
                cnt = 0
            res.append(cnt)
        return res

# leetcode 739
# 시간 초과
