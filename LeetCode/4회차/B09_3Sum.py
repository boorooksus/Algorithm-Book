from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3:
            return []

        nums.sort()

        res = {}
        for mid in range(1, len(nums) - 1):
            left, right = mid - 1, mid + 1
            while left >= 0 and right < len(nums):
                window = nums[left] + nums[mid] + nums[right]

                if window < 0:
                    right += 1
                elif window > 0:
                    left -= 1
                else:
                    res[nums[left], nums[mid], nums[right]] = 0
                    left -= 1

        return list(res.keys())


print(Solution().threeSum([0,0,0]))
