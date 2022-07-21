from typing import List
from sys import setrecursionlimit
setrecursionlimit(10 ** 9)


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        half = len(nums) // 2
        a = self.majorityElement(nums[:half])
        b = self.majorityElement(nums[half:])

        return [a, b][nums.count(a) <= half]


print(Solution().majorityElement([3,2, 3]))
