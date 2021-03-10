from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0

        if len(s) <= k + 1:
            return len(s)

        res = 0

        left, right = 0, 0
        cnt = Counter()

        while right < len(s):
            cnt[s[right]] += 1
            need = right - left + 1 - cnt.most_common(1)[0][1]

            if need <= k:
                res = right - left + 1
                right += 1
            else:
                cnt[s[left]] -= 1
                left += 1
                right += 1

        return res


print(Solution().characterReplacement(
"AABABBA",
1
                                      ))