from typing import List
import sys


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = 0
        best_sum = -sys.maxsize

        for num in nums:
            cur_sum = max(num, cur_sum + num)
            best_sum = max(best_sum, cur_sum)

        return best_sum
