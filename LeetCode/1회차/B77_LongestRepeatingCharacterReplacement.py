from collections import deque, defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0

        ans = 0
        start, end = 0, 0
        cnt = defaultdict(int)

        cnt[s[0]] += 1

        while end < len(s):
            if max(cnt.values()) + k >= sum(cnt.values()):
                if end - start + 1 > ans:
                    ans = end - start + 1
                end += 1
                if end < len(s):
                    cnt[s[end]] += 1

            else:
                cnt[s[start]] -= 1
                start += 1
        return ans


sol = Solution()
print(sol.characterReplacement("AABABBA", 1))

"""
leetcode: 424
처음에 Counter 사용했다가 시간 초과
"""

