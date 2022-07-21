from collections import Counter


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        left = 0
        cnt = Counter()
        res = 0

        for right in range(len(s)):
            cnt[s[right]] += 1
            while cnt.most_common(1)[0][1] > 1:
                cnt[s[left]] -= 1
                # cnt = Counter(cnt)
                left += 1
            res = max(res, right - left + 1)

        return res


print(Solution().lengthOfLongestSubstring("abcabcbb"))