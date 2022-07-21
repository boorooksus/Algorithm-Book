class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a, b = list(s), list(t)
        while a:
            cur = a.pop()
            if cur not in b:
                return False
            b.remove(cur)

        if b:
            return False

        return True

"""
leetcode: 242
"""