from collections import deque
import re

class Solution:
    def isPalindrome(self, s:str) -> bool:
        dq = deque()
        for i in s:
            if i.isalnum():
                dq.append(i.lower())
        while len(dq) > 1:
            if dq.popleft() != dq.pop():
                return False
        return True


sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))