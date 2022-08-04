from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = 10000
        res = 0
        for price in prices:
            res = max(price - low, res)
            if price < low:
                low = price
        return res


print(Solution().maxProfit([7,1,5,3,6,4]))
