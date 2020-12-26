from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        letters: List[List[str]] = [[],
                                    [], ["a", "b", "c"], ["d", "e", "f"],
                                    ["g", "h", "i"], ["j", "k", "l"], ["m", "n", "o"],
                                    ["p", "q", "r", "s"], ["t", "u", "v"], ["w", "x", "y", "z"]
                                    ]
        ans: List = []

        def dfs(cur: str, digits: str):
            if digits == "":
                ans.append(cur)
                return

            digit: int = int(digits[0])

            for letter in letters[digit]:
                dfs(cur + letter, digits[1:])

        dfs("", digits)

        return ans

# leetcode: 17
# dfs
# 딕셔너리 활용 가능
