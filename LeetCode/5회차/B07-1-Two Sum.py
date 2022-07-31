from typing import List
from bisect import bisect_left


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = list((nums[i], i) for i in range(len(nums)))
        temp.sort()
        for i, (num, idx) in enumerate(temp):
            j = bisect_left(nums, target - nums[i], i + 1)
            while i < j < len(temp) and num + temp[j][0] == target:
                if i < j < len(temp) and num + temp[j][0] == target:
                    return [idx, temp[j][1]]
        return [0, 0]


print(Solution().twoSum([3,2,4],
6))
