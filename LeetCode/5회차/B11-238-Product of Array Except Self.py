from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        left, right = 0, len(nums) - 1
        left_multi, right_multi = 1, 1
        while right >= 0:
            res[left] *= left_multi
            res[right] *= right_multi
            left_multi *= nums[left]
            right_multi *= nums[right]
            left += 1
            right -= 1
        return res


print(Solution().productExceptSelf([1,2,3,4]))
