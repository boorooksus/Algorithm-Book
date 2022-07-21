class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted([char for char in s]) == sorted([char for char in t])

