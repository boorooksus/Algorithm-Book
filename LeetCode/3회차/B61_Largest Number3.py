from typing import List


class Solution:
    @staticmethod
    def to_swap(x: int, y: int) -> bool:
        return str(x) + str(y) < str(y) + str(x)

    def largestNumber(self, nums: List[int]) -> str:
        i = 0
        while i < len(nums):
            j = i
            while j > 0 and self.to_swap(nums[j - 1], nums[j]):
                nums[j - 1], nums[j] = nums[j], nums[j - 1]
                j -= 1
            i += 1
        return str(int(''.join(str(num) for num in nums)))


print(Solution().largestNumber([3,30,34,5,9]))
