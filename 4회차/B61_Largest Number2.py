from typing import List


class Solution:
    @staticmethod
    def to_swap(a: int, b: int) -> bool:
        return str(a) + str(b) < str(b) + str(a)

    def largestNumber(self, nums: List[int]) -> str:
        i = 1

        while i < len(nums):
            j = i
            while j > 0 and self.to_swap(nums[j - 1], nums[j]):
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                j -= 1
            i += 1

        return str((int(''.join(map(str, nums)))))


print(Solution().largestNumber([29,48,64,80,33,87,27,8,35,42]))