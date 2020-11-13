from typing import List
from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 리스트 반환(경고 표시 없음)
        # return list(list(zip(*Counter(nums).most_common(k)))[0])
        # 튜플로 반환(이것도 정답)
        return list(zip(*Counter(nums).most_common(k)))[0]


sol = Solution()
print(sol.topKFrequent([5,3,1,1,1,3,73,1], 2))

# leetcode: 347
# 파이썬 다운 방식
# zip, *(umpack) 이용

