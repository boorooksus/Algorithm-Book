from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def runner(x):
            xs = str(x)
            return int(x + (9 - len(str(x))) * x[-1])

        ns = []
        for num in nums:
            ns.append(str(num))
        ns.sort(reverse=True, key=lambda x:runner(x))
        return ''.join(ns)


print(Solution().largestNumber(
[3,30,34,5,9]))

"""
34 3 31
343233333 3432222222
"""