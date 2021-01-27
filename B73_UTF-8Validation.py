from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def get_len(first: int) -> int:
            if first & 0b10000000 == 0:
                return 1
            cur = 2
            mask = 0b100000
            while cur < 5:
                if first & mask == 0:
                    return cur
                cur += 1
                mask >>= 1
            return -1

        start = 0
        while start < len(data):
            byte_len = get_len(data[0])

            if byte_len == -1:
                return False
            if byte_len == 1:
                return True

            first, second = 0b10000000, 0b1000000

            if len(data) - start < byte_len:
                return False

            for bits in data[start + 1:byte_len]:
                if bits & first == 0 or bits & second == second:
                    return False
            start += 4

        # if len(data) > byte_len:
        #     for i in range(byte_len, len(data)):
        #         x = data[i] & first
        #         y = data[i] & second
        #         if data[i] & first == first and data[i] & second == 0:
        #             return False

        return True


sol = Solution()
print(sol.validUtf8([240, 162, 138, 147, 145]))
# print(sol.validUtf8([237]))
# print(sol.validUtf8([197,130,1]))

# 0b11110000 0b10100010 0b10001010 0b10010011 0b10010001



"""
leetcode: 393
오답.
"""