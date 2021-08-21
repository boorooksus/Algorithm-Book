from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        result = []
        letters = {}
        for i in range(2, 7):
            letters[i] = ''.join(chr(97 + (i - 2) * 3 + j) for j in range(3))
        letters[7] = "pqrs"
        letters[8] = "tuv"
        letters[9] = "wxyz"

        def dfs(index, word):
            if index == len(digits):
                result.append(word)
                return

            for letter in letters[int(digits[index])]:
                dfs(index + 1, word + letter)

        dfs(0, "")
        return result


print(Solution().letterCombinations("23"))

