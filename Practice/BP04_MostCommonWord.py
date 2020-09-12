from typing import List
from collections import defaultdict
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        paragraph = re.sub('[^a-zA-Z0-9]',' ',paragraph)
        words = paragraph.split()
        dic = defaultdict(int)
        max_word: str = ''
        max_cnt: int = 0
        for word in words:
            if word not in banned:
                dic[word] += 1
                if dic[word] > max_cnt:
                    max_word = word
                    max_cnt = dic[word]
        return max_word

sol = Solution()
print(sol.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))