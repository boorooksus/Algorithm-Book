from typing import List
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        paragraph = re.sub('[^a-zA-Z0-9 ]', '', paragraph)
        words = paragraph.split()
        cnt = dict()
        max_word = ''
        max_cnt = 0
        for word in words:
            if word in banned:
                continue
            if word not in cnt:
                cnt[word] = 1
            else:
                cnt[word] += 1
            if cnt[word] >= max_cnt:
                max_word = word
                max_cnt = cnt[word]
        return max_word