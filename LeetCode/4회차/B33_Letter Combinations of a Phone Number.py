from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(digits: str, letters: str):
            if not digits:
                res.append(letters)
                return

            for char in table[digits[0]]:
                dfs(digits[1:], letters + char)

        table = {'2': 'abc', '3': 'def', '4': 'ghi',
                 '5': 'jkl', '6': 'mno', '7': 'pqrs',
                 '8': 'tuv', '9': 'wxyz'}

        if not digits:
            return []

        res = []
        dfs(digits, '')
        return res
