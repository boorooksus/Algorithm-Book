from typing import List


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def check(word: str) -> bool:
            return True if word == word[::-1] else False

        res = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue
                if len(words[i]) > 0 and len(words[j]) > 0 and \
                        words[i][0] != words[j][-1]:
                    continue

                if check(words[i] + words[j]):
                    res += [i, j],
        return res
