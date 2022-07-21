from typing import List
from collections import Counter


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # return Counter(nums).most_common()[-1][0]
        li = {}
        for num in nums:
            if num in li:
                li.pop(num)
            else:
                li[num] = 1
        return list(li.keys())[0]
