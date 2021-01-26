from typing import List


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # x = bin(x ^ y)
        # return x.count('1')
        return bin(x ^ y).count('1')


"""
leetcode: 461

"""