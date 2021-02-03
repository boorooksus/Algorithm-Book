from typing import List
from sys import setrecursionlimit
setrecursionlimit(10 ** 9)

class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        def cal(a, b, op: str):
            res = []
            for i in a:
                for j in b:
                    res.append(eval(str(i) + op + str(j)))
            return res

        if input.isdigit():
            return [int(input)]

        res = []
        for i, val in enumerate(input):
            if val in "+-*":
                a = self.diffWaysToCompute(input[:i])
                b = self.diffWaysToCompute((input[i + 1:]))
                res.extend(cal(a, b, val))
        return res


print(Solution().diffWaysToCompute("2*3-4*5"))


"""
leetcode: 241
분할정복
"""