from collections import Counter

class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')

print(Solution().hammingWeight(1011))