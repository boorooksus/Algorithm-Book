

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expansion(left: int, right: int) -> str:
            while left >= 0 and right <= len(s) and s[left] == s[right - 1]:
                left -= 1
                right += 1
            return s[left + 1: right - 1]

        if s == s[::-1] or len(s) == 1:
            return s

        res = s[0]
        for i in range(len(s)):
            x = expansion(i, i + 1)
            y = expansion(i, i + 2)
            res = max(res, expansion(i, i + 1), expansion(i, i + 2), key=len)

        return res


sol = Solution()
print(sol.longestPalindrome("babad"))


# 시간 초과