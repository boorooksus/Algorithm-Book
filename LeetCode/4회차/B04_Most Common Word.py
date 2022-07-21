from typing import List
from collections import Counter
import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.sub(r'[^ a-z]', ' ', paragraph.lower()).split()
        cnt = Counter(words)

        while cnt:
            word = cnt.most_common(1)[0][0]
            if word not in banned:
                return word
            cnt.pop(word)
        return None


print(Solution().mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.",
["hit"]))
