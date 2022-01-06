import sys
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        low, high = sys.maxsize, 0

        for price in prices:
            if low < price:
                high = price
                profit = max(profit, high - low)

            if price < low:
                low, high = price, 0

        return profit
