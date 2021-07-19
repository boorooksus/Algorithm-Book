from typing import List
import sys


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_sum = -sys.maxsize
        cur_sum = 0

        for num in nums:
            cur_sum = max(num, cur_sum + num)
            best_sum = max(best_sum, cur_sum)

        return best_sum


print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))