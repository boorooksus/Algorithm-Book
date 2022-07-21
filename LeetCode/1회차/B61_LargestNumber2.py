from typing import List


class Solution:
    @staticmethod
    def compare(a, b) -> bool:
        x = str(a) + str(b)
        y = str(b) + str(a)
        return x < y

    def largestNumber(self, nums: List[int]) -> str:
        for i in range(1, len(nums)):
            j = i
            while j > 0 and self.compare(nums[j - 1], nums[j]):
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                j -= 1

        return str(int(''.join(map(str, nums))))


sol = Solution()
print(sol.largestNumber([3,30,34,5,9]))


"""
leetcode: 179
삽입 정렬을 이용한 풀이
"""