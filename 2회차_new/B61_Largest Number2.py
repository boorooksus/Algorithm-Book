from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(a: int, b: int) -> bool:
            return int(str(a) + str(b)) < int(str(b) + str(a))

        i = 1
        while i < len(nums):
            j = i
            while j > 0 and compare(nums[j - 1], nums[j]):
                nums[j - 1], nums[j] = nums[j], nums[j - 1]
                j -= 1
            i += 1
        return str(int(''.join(map(str, nums))))


print(Solution().largestNumber(
[3,30,34,5,9]))

"""
34 3 31
343233333 3432222222
"""