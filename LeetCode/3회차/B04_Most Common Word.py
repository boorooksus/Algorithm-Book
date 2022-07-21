from typing import List
from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        for char in paragraph:
            if ord(char) < 97 or ord(char) > 122:
                paragraph = paragraph.replace(char, ' ')

        counts = Counter(paragraph.split())
        for word, count in counts.most_common():
            if word not in banned:
                return word


print(Solution().mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.",
["hit"]))