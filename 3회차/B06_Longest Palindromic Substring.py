class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(s):
            return s == s[::-1]

        if not s:
            return ""

        result = s[0]
        for i in range(len(s) - 1):
            for j in range(1, len(s)):
                if check(s[i:j + 1]) and len(result) < j - i + 1:
                    result = s[i:j + 1]
        return result


print(Solution().longestPalindrome("bb"))
