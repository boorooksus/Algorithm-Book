from typing import List
import sys

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = sys.maxsize
        max_profit = 0
        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, prices[i] - min_price)
        return max_profit

# 리트코드: 121
# 카데인 알고리즘.
# 시간복잡도: O(N)
