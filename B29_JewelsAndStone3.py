class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum(s in J for s in S)


# leetcode: 771
# 파이썬 다운 방식
