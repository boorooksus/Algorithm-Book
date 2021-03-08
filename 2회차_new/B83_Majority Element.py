from typing import List
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return Counter(nums).most_common(1)[0][0]


print(Solution().majorityElement([3,2,3]))
