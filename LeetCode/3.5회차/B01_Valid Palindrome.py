import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('\W|_', '', s)
        return s.lower() == s.lower()[::-1]
