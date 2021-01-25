from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, num in enumerate(numbers):
            start, end = i + 1, len(numbers) - 1
            while start <= end:
                mid = start + (end - start) // 2
                if numbers[mid] < target - num:
                    start = mid + 1

                elif numbers[mid] > target - num:
                    end = mid - 1
                else:
                    return [i + 1, mid + 1]
        return []

sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))
# print(sol.twoSum([0, 0], 0))

"""
leetcode: 167
이진 탐색
"""