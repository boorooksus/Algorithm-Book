from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        needs = Counter()
        for char in t:
            needs[char] += 1

        left, right = 0, 0
        needs[s[0]] -= 1
        res = ""

        while left <= right:
            if max(needs.values()) > 0:
                right += 1
                if right >= len(s):
                    break
                needs[s[right]] -= 1

            else:
                if res == "" or len(res) > right - left + 1:
                    res = s[left: right + 1]
                # res = min(res, s[left: right + 1], key=lambda x:len(x))
                needs[s[left]] += 1
                left += 1

        return res


# print(Solution().minWindow("ADOBECODEBANC", "ABC"))
print(Solution().minWindow("a",
"aa"))