import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = re.sub(r'[^\w]| |_', '', s)
        x = x.lower()
        return x == x[::-1]


print(Solution().isPalindrome("ab_a"))
