import sys
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        low = sys.maxsize

        for price in prices:
            low = min(low, price)
            profit = max(profit, price - low)

        return profit
