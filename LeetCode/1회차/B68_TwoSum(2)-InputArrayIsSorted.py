from typing import List
import bisect


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, num in enumerate(numbers):
            pair = target - num
            idx = bisect.bisect_left(numbers[i + 1:], pair)
            idx += i + 1
            if 0 <= idx < len(numbers) and numbers[idx] == pair:
                return [i + 1, idx + 1]

        return []

sol = Solution()
print(sol.twoSum([2,7,11,15], 9))
#print(sol.twoSum([0, 0], 0))

"""
leetcode: 167
"""