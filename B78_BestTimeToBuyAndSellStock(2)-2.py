from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(max(0, prices[i + 1] - prices[i]) for i in range(len(prices) - 1))

sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))

"""
leetcode 122
그리디 알고리즘
파이썬 다운 풀이
"""

