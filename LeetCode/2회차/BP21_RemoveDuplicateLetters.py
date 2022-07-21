from collections import defaultdict

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        for char in sorted(set(s)):
            suffix = s[s.index(char):]
            if set(suffix) == set(s):
                return char + self.removeDuplicateLetters(suffix.replace(char, ''))
        return ''

# leetcode: 316
# 다시 풀어볼 것
