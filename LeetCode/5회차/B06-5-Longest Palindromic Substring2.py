class Solution:
    def expand(self, s: str, start: int, end: int) -> str:
        while start >= 0 and end < len(s) and s[start] == s[end]:
            start -= 1
            end += 1
        return s[start + 1:end]

    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2 or s == s[::-1]:
            return s

        ans = s[0]
        for i in range(len(s)):
            ans = max(self.expand(s, i - 1, i + 1),
                      self.expand(s, i, i + 1),
                      ans,
                      key=len)
        return ans


print(Solution().longestPalindrome("babad"))