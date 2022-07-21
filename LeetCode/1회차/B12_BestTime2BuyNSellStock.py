from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices) - 1):
            max_profit = max(max_profit, max(prices[i + 1:])- prices[i])
        return max_profit

# 리트코드: 121
