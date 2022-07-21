from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        check = []
        for num in nums:
            if num not in check:
                check.append(num)
            else:
                check.remove(num)
        return check[0]