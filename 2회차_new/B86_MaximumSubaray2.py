from typing import List
from sys import maxsize

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = 0
        best_sum = -maxsize

        for num in nums:
            cur_sum = max(num, cur_sum + num)
            best_sum = max(cur_sum, best_sum)

        return best_sum



print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
