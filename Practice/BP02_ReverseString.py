from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        s = s[::-1]
        print(s)

sol = Solution()
sol.reverseString(["h","e","l","l","o"])

# 틀림. reverse가 안됨