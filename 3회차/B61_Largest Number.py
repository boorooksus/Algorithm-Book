from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_str = [str(num) for num in nums]
        nums_str.sort(reverse=True, key=lambda x: x + (10 - len(x)) * x[-1])
        return ''.join(nums_str)


print(Solution().largestNumber([3,30,34,5,9]))

"""
실패
3 30 > 30 3
3432 34323 > 34323 3432
"""