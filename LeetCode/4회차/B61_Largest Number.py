from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strs = sorted(list(map(str, nums)), reverse=True)

        res = ''.join(strs)
        for i in range(len(strs)):
            for j in range(len(strs)):
                strs[i], strs[j] = strs[j], strs[i]
                temp = ''.join(strs)
                if res < temp:
                    res = temp
                else:
                    strs[i], strs[j] = strs[j], strs[i]

        while res[0] == '0' and len(res) > 1:
            res = res[1:]
        return res


print(Solution().largestNumber([29,48,64,80,33,87,27,8,35,42]))