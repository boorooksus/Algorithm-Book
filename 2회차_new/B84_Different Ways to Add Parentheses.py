from typing import List


class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        def cal(a, b, op):
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
                b = self.diffWaysToCompute(input[i + 1:])
                res += cal(a, b, val)
        return res
