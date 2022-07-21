from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def check(byte: int, start: int) -> int:
            for i in range(1, byte):
                if start + i >= len(data) or data[start + i] >> 6 != 0b10:
                    return False
            return True

        i = 0
        while i < len(data):
            if data[i] >> 7 == 0:
                i += 1
            elif data[i] >> 5 == 0b110 and check(2, i):
                i += 2
            elif data[i] >> 4 == 0b1110 and check(3, i):
                i += 3
            elif data[i] >> 3 == 0b11110 and check(4, i):
                i += 4
            else:
                return False
        return True
