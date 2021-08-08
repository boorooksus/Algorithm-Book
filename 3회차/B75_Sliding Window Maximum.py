from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = [max(nums[:k])]

        left = 0

        for right in range(k, len(nums)):
            if nums[left] < result[-1]:
                if result[-1] < nums[right]:
                    result.append(nums[right])
                else:
                    result.append(result[-1])
            else:
                result.append(max(nums[left + 1: right + 1]))

            left += 1

        return result



