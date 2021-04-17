from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def get_byte(num: int) -> int:
            num_str = str(bin(num))[2:]
            if len(num_str) < 8:
                num_str = '0' * (8 - len(num_str)) + num_str
            idx = 0
            while idx < len(num_str) and num_str[idx] == '1':
                idx += 1
            if idx == 1:
                return -1

            return idx if idx != 0 else 1

        cur = 0
        while cur < len(data):
            byte = get_byte(data[cur])
            if byte == -1:
                return False

            for i in range(cur + 1, cur + byte):
                if i >= len(data):
                    return False
                num = bin(data[i])[2:]
                num = '0' * (8 - len(num)) + num

                if num[0] != '1' or num[1] != '0':
                    return False
            cur += byte

        return True


print(Solution().validUtf8(
[250,145,145,145,145]))


# 실패
# 인풋이 [250,145,145,145,145] 일때 False여야 하는데 True가 뜸
# ---왜 이게 False인지 모르겠다...---
# UTF8 can be from 1 to 4 bytes long 라서 4바이트를 넘길 수 없음...