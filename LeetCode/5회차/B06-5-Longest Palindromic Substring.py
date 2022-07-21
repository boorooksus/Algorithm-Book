class Solution:
    def __init__(self):
        self.ans = ''

    def check(self, s: str, start: int, end: int) -> (int, int):
        while start >= 0 and end < len(s) and s[start] == s[end]:
            start -= 1
            end += 1

        if end - start - 1 > len(self.ans):
            self.ans = s[start + 1:end]

    def longestPalindrome(self, s: str) -> str:
        self.ans = s[0]
        for i in range(len(s)):
            self.check(s, i - 1, i + 1)
            self.check(s, i, i + 1)
        return self.ans


print(Solution().longestPalindrome('bb'))