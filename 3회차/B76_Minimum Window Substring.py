from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        result = "x" * 100000
        needs = Counter(t)

        for right in range(1, len(s) + 1):
            needs[s[right - 1]] -= 1

            while needs.most_common(1)[0][1] <= 0:
                result = s[left:right] if len(result) > right - left else result
                needs[s[left]] += 1
                left += 1

        if len(result) == 100000:
            result = ""
        return result


print(Solution().minWindow("ADOBECODEBANC",
"ABC"))