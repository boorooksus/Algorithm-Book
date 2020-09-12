from typing import List
import sys


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, min_price = 0, sys.maxsize
        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, prices[i] - min_price)
        return max_profit


# 다시 풀 것!!
