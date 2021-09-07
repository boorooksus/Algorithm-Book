from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red, white, blue = 0, 0, len(nums)
        mid = 1
        while white < blue:
            if nums[white] < mid:
                nums[red], nums[white] = nums[white], nums[red]
                red += 1
                white += 1
            elif nums[white] > mid:
                blue -= 1
                nums[white], nums[blue] = nums[blue], nums[white]
            else:
                white += 1


"""
leetcode: 75
국기 문제
"""