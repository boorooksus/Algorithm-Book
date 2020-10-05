from collections import defaultdict

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = defaultdict(int)
        for jewel in J:
            jewels[jewel] += 1

        ans = 0
        for stone in S:
            if jewels[stone] > 0:
                ans += 1
        return ans


# leetcode: 771
# 내 풀이
