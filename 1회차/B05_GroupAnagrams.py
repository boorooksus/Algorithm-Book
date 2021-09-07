from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
        return anagrams.values()


# leetcode 49번
# defaultedict, join
# 문자열 -> 리스트 -> 정렬 -> 다시 문자열