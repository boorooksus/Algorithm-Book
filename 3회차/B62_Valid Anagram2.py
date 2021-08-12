class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_bit, t_bit = 0, 0
        for char in s:
            s_bit += ord(char)
        for char in t:
            t_bit += ord(char)
        return s_bit == t_bit


print(Solution().isAnagram("aa",
"bb"))

"""
실패
"""