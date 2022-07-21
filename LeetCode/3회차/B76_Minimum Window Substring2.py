from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        start = end = left = 0
        needs = Counter(t)
        missing = len(t)

        for right, char in enumerate(s, 1):
            missing -= needs[char] > 0
            needs[char] -= 1

            if missing == 0:
                while left < right and needs[s[left]] < 0:
                    needs[s[left]] += 1
                    left += 1

                if not end or right - left <= end - start:
                    start, end = left, right

                needs[s[left]] += 1
                missing += 1
                left += 1

        return s[start:end]


print(Solution().minWindow("ADOBECODEBANC",
"ABC"))