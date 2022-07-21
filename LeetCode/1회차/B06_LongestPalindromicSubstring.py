

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
        max_len = 0
        lp = ''
        for i in range(len(s)):
            for j in range(i, len(s)):
                x = s[i: j + 1]
                y = s[j:: -1]
                z = j - i + 1
                if i != 0 and s[i: j + 1] == s[j: i - 1: -1] and j - i + 1 >= max_len:
                    max_len = j - i + 1
                    lp = s[i:j + 1]
                elif i == 0 and s[0: j + 1] == s[j:: -1] and j - i + 1 >= max_len:
                    max_len = j - i + 1
                    lp = s[i:j + 1]
        return lp


sol = Solution()
print(sol.longestPalindrome("ab"))


# 시간 초과