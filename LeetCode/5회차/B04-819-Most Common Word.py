from typing import List
from re import sub
from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        cnts = Counter(sub(r'[^a-z ]', ' ', paragraph.lower()).split())
        for word, cnt in cnts.most_common():
            if word not in banned:
                return word

        return ''
