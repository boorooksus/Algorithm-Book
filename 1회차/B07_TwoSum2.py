from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, num in enumerate(nums):
            temp = target - num

            if temp in nums[idx + 1:]:
                return [idx, nums[idx + 1:].index(temp) + idx + 1]


# leetcode: 01
# in 을 이용한 탐색이 1번 풀이보다 좀 더 빠름
# 그래도 시간복잡도는 똑같이 O(N^2)
