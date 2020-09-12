from typing import List


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expansion(start: int, end: int) -> str:
            while start >= 0 and end < len(s) and s[start] == s[end]:
                start -= 1
                end += 1
            return s[start + 1: end]

        res = ''
        for i in range(len(s)):
            res = max(res, expansion(i, i), expansion(i, i + 1), key=lambda x: len(x))
        return res


sol = Solution()
print(sol.longestPalindrome("babad"))