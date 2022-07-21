from typing import List
from collections import defaultdict
import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.sub(r'[^ a-z]', ' ', paragraph.lower()).split()
        cnts = defaultdict(int)
        for word in words:
            if word not in banned:
                cnts[word] += 1
        words.sort(key=lambda x: cnts[x], reverse=True)

        return words[0]


print(Solution().mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.",
["hit"]))
