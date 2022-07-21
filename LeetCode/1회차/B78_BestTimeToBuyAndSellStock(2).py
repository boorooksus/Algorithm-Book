from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        prev = prices[0]

        for price in prices[1:]:
            if price > prev:
                res += price - prev
            prev = price

        return res

sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))

"""
leetcode 122
그리디 알고리즘
"""

