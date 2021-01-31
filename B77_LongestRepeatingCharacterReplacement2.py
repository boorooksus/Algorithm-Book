from collections import Counter, defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0

        left = right = 0
        cnt = Counter()

        for right in range(1, len(s) + 1):
            cnt[s[right - 1]] += 1

            if right - left > cnt.most_common(1)[0][1] + k:
                cnt[s[left]] -= 1
                left += 1

        return right - left


sol = Solution()
print(sol.characterReplacement("AABABBA", 1))

"""
leetcode: 424
"""

