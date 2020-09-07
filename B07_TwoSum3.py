from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_idx = dict()
        for idx, num in enumerate(nums):
            num_idx[num] = idx

        for idx, num in enumerate(nums):
            temp = target - num
            if temp in num_idx and idx != num_idx[temp]:
                return [idx, num_idx[temp]]


# leetcode: 01
# dict: hash table로 구현 => 2번 풀이보다 더 빠름
# 시간 복잡도 : O(N)
