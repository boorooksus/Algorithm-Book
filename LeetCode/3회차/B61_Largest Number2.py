from typing import List
from itertools import permutations


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        result = ''
        nums_str = [str(num) for num in nums]

        for num_tuple in permutations(nums_str):
            result = max(result, ''.join(num_tuple))

        idx = 0
        while idx < len(result) - 1 and result[idx] == '0':
            idx += 1
        if idx > 0:
            result = result[idx:]

        return result


print(Solution().largestNumber([0,0,0]))

"""
시간초과
"""