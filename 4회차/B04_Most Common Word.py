from typing import List
from collections import Counter
import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = list(re.sub('\W|_', ' ', paragraph.lower()).split())
        counts = Counter(words).most_common()
        for word, cnt in counts:
            if word not in banned:
                return word
