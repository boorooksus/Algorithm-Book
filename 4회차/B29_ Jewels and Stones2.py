from collections import defaultdict


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        cnt = defaultdict(int)
        for jewel in jewels:
            cnt[jewel] += 1
        res = 0
        for stone in stones:
            res += cnt[stone]
        return res
