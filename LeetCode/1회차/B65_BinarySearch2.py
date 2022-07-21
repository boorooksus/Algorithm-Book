from typing import List
from sys import setrecursionlimit
setrecursionlimit(10 ** 9)


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bs(start, end):
            if start > end:
                return -1

            # === 1 ========================
            mid = start + (end - start) // 2

            if nums[mid] < target:
                return bs(mid + 1, end)
            elif nums[mid] > target:
                return bs(start, mid - 1)
            else:
                return mid

        return bs(0, len(nums) - 1)


sol = Solution()
print(sol.search([-1,0,3,5,9,12], 3))


"""
leetcode: 704
재귀 이용한 방식
1: mid = '(start + end) // 2' 대신 이렇게 쓴 이유:
    start + end가 자료형 범위를 넘어설 경우 오버플러우 발생하므로
"""