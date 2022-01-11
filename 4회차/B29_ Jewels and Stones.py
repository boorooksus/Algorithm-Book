from collections import Counter


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # res = 0
        # for jewel in jewels:
        #     res += stones.count(jewel)
        # return res
        cnt = Counter(stones)
        res = 0
        for jewel in jewels:
            res += cnt[jewel]
        return res
