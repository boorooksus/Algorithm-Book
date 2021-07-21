from typing import List

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def cal(a: List[int], b: List[int], op: str):
            res = []
            for i in a:
                for j in b:
                    res.append(eval(str(i) + op + str(j)))
            return res

        if expression.isdigit():
            return [int(expression)]

        res = []
        for i, val in enumerate(expression):
            if val in "+-*":
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i + 1:])
                res += cal(left, right, val)
        return res
