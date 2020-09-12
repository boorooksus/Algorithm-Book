from collections import deque
import re

class Solution:
    def isPalindrome(self, s:str) -> bool:
        s = s.lower()
        s = re.sub('[^a-zA-Z0-9]', '', s)
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))