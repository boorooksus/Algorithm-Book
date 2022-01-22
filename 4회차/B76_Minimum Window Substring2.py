from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnt = Counter(t)
        need = len(t)

        start, end = 0, 0
        left = 0

        for right, char in enumerate(s):
            need -= cnt[char] > 0
            cnt[char] -= 1

            if need == 0:
                while left < right and cnt[s[left]] < 0:
                    cnt[s[left]] += 1
                    left += 1

                if not end or right - left < end - start:
                    start, end = left, right + 1
                cnt[s[left]] += 1
                need += 1
                left += 1
        return s[start:end]


print(Solution().minWindow("a",
"aa"))



