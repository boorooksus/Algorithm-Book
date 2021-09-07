from typing import List
from bisect import bisect_left


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, num in enumerate(numbers):
            idx = bisect_left(numbers, target - num, i + 1)
            if 0 <= idx < len(numbers) and num + numbers[idx] == target:
                return [i + 1, idx + 1]
        return []

sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))
# print(sol.twoSum([0, 0], 0))

"""
leetcode: 167
bisect 풀이 개선. 속도가 더 빠름
슬라이싱 사용 안하고 bisect_left의 세 번째 인자로 범위를 지정 
"""