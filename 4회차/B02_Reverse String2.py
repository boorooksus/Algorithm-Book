from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # 다른 풀이1
        # s[:] = s[::-1]

        # 다른 풀이2
        s.reverse()


Solution().reverseString(
["h","e","l","l","o"])