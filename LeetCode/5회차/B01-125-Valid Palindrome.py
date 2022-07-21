from re import sub


class Solution:
    def check(self, s: str) -> bool:
        return s == s[::-1]

    def isPalindrome(self, s: str) -> bool:
        return self.check(sub(r'[^A-Z\d]', '', s.upper()))


print(Solution().isPalindrome("A man, a plan, a canal: Panama"))