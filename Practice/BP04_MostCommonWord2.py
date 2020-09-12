from typing import List
from collections import Counter
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = list(word for word in re.sub(r'[^\w]', ' ', paragraph.lower()).split() if word not in banned)
        cnt = Counter(words)
        return cnt.most_common(1)[0][0]

sol = Solution()
print(sol.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))