from collections import Counter

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        freq = Counter(S)

        ans = 0
        for j in J:
            # key가 freq에 없어도 에러가 아닌 0이 리턴됨
            ans += freq[j]
        return ans


# leetcode: 771
# Counter 활용
