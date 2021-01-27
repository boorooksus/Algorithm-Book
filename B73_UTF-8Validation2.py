from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def check(size: int) -> bool:
            for i in range(start + 1, start + size):
                if i >= len(data) or data[i] >> 6 != 0b10:
                    return False
            return True

        start, size = 0, 0

        while start < len(data):
            if data[start] >> 3 == 0b11110:
                size = 4
            elif data[start] >> 4 == 0b1110:
                size = 3
            elif data[start] >> 5 == 0b110:
                size = 2
            elif data[start] >> 7 == 0b0:
                size = 1
            else:
                return False

            if not check(size):
                return False
            start += size
        return True


sol = Solution()
print(sol.validUtf8([240, 162, 138, 147, 145]))
# print(sol.validUtf8([237]))
# print(sol.validUtf8([197,130,1]))

# 0b11110000 0b10100010 0b10001010 0b10010011 0b10010001



"""
leetcode: 393
"""