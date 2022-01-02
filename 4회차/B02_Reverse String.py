from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        """ 풀이1 """
        # s[:] = s[::-1]

        """ 풀이2 """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        """ 풀이3 """
        s.reverse()
