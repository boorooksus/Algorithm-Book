from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        res = ""
        dic = {}
        for i in nums:
            dic[i] = (str(i) * 10)[:10]
            # 우선 순위 관계가 비교 가능하도록 값을 만든다.

        for i in sorted(nums, key=lambda x: dic[x], reverse=True):
            res += str(i)

        if int(res) == 0:
            res = "0"
        return res

sol = Solution()
print(sol.largestNumber([3,30,34,5,9]))


"""
leetcode: 179
"""