class Solution:
    def longestPalindrome(self, s: str) -> str:

        def check(start: int, end: int) -> str:
            while 0 <= start and end < len(s) and s[start] == s[end]:
                start -= 1
                end += 1

            return s[start + 1:end]

        if len(s) < 2 or s == s[::-1]:
            return s

        res = ''
        for i in range(len(s)):
            res = max(res, check(i - 1, i + 1), check(i, i + 1), key=len)

        return res


print(Solution().longestPalindrome("bb"))