import sys
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        low, high = sys.maxsize, -sys.maxsize

        for i in range(len(prices)):
            if prices[i] < low:
                low = prices[i]
                high = -sys.maxsize

            if prices[i] > high:
                high = prices[i]
                result = max(result, high - low)

        return result