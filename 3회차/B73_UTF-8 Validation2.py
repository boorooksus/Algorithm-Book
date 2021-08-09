from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def check(v):
            for i in range(start + 1, start + v):
                if i >= len(data) or data[i] >> 6 != 0b10:
                    return False
            return True

        start = 0
        while start < len(data):
            first = data[start]
            if first >> 7 == 0b0 and check(1):
                start += 1
            elif first >> 5 == 0b110 and check(2):
                start += 2
            elif first >> 4 == 0b1110 and check(3):
                start += 3
            elif first >> 3 == 0b11110 and check(4):
                start += 4
            else:
                return False
        return True

print(Solution().validUtf8(
[240,162,138,147]))
"""
[240,162,138,147]
11110000, 10100010, 10001010, 10010011

[235,140,4]
11101011, 10001100, 00000100
"""