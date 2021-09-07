from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        counter = Counter(nums)
        temp = sorted(counter, key=lambda x: counter[x], reverse=True)
        for i in range(k):
            ans.append(temp[i])
        return ans


sol = Solution()
print(sol.topKFrequent([4,1,-1,2,-1,2,3], 2))

# leetcode: 347
# 정답
