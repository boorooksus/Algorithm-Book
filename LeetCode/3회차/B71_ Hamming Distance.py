class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        result = 0
        while x or y:
            if bin(x)[-1] != bin(y)[-1]:
                result += 1
            x = x >> 1
            y = y >> 1
        return result
