from typing import List
from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        freq, ans = [], []
        for num in counter:
            heapq.heappush(freq, (-counter[num], num))
        for i in range(k):
            # === 1 =====================================
            ans.append(heapq.heappop(freq)[1])
        return ans


sol = Solution()
print(sol.topKFrequent([5,3,1,1,1,3,73,1], 2))

# leetcode: 347
# heapq 이용 방식
# 1: heappop 사용 안하고 freq[i][1]을 사용할 경우 틀림
# (freq는 오름차순이 아닌 heap 방식으로 정렬됐기 때문)
