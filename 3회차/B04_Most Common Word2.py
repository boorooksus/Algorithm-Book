from typing import List
from collections import Counter
import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        return Counter([word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]).most_common(1)[0][0]

print(Solution().mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.",
                                ["hit"]))
