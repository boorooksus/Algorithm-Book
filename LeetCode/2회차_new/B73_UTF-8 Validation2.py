from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def check(byte):
            for i in range(start + 1, start + byte):
                if i >= len(data) or data[i] >> 6 != 0b10:
                    return False
            return True

        start = 0
        while start < len(data):
            first = data[start]
            if first < 0b10000000:
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
[250,145,145,145,145]))

