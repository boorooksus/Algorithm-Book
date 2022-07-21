from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        result = 0
        last = prices[0]
        for i, v in enumerate(prices, 1):
            if last < v:
                result += v - last
            last = v
        return result
