from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(nums)):
            target = nums[i]
            for j in range(i + 1, len(nums)):
                temp = [target, nums[j], -(target + nums[j])]
                temp.sort()
                if -(target + nums[j]) in nums[j + 1:] and temp not in res:
                    res.append(temp)

        return res


sol = Solution()
print(sol.threeSum([1, -1, -1, 0]))

# 시간 초과
