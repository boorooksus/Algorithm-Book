from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnt = Counter()
        for char in t:
            cnt[char] += 1

        left = 0
        res = ''
        for right in range(len(s)):
            if s[right] in t:
                cnt[s[right]] -= 1

            while cnt.most_common(1)[0][1] <= 0:
                if not res or right - left + 1 < len(res):
                    res = s[left:right + 1]
                if s[left] in t:
                    cnt[s[left]] += 1
                left += 1
        return res


print(Solution().minWindow("ADOBECODEBANC",
"ABC"))



