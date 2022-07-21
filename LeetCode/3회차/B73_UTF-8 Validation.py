from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def encoding(v):
            bits = bin(v)[2:]
            if len(bits) < 8:
                bits = '0' * (8 - len(bits)) + bits
            return bits

        def getChar(v):
            bits = encoding(v)
            if bits[0] == '0':
                return 1
            elif bits[0:3] == "110":
                return 2
            elif bits[0:4] == '1110':
                return 3
            elif bits[0:5] == '11110':
                return 4
            else:
                return -1

        i = 0
        while i < len(data):
            char = getChar(data[i])
            if char == -1:
                return False
            for j in range(i + 1, i + char):
                if j == len(data):
                    return False
                bits = encoding(data[j])
                if bits[:2] != '10':
                    return False
            i += char

        return True


print(Solution().validUtf8([237]))
"""
[235,140,4]
11101011, 10001100, 00000100
"""