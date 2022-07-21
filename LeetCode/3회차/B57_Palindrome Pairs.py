from typing import List
from itertools import permutations


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:

        result = []
        for x, y in permutations(words, 2):
            if x + y == (x + y)[::-1]:
                result += [words.index(x), words.index(y)],

        return result
