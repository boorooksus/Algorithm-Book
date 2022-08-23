from collections import defaultdict, deque


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s or len(s) == 1:
            return len(s)

        start = 0
        ans = 0
        while start < len(s):
            end = start
            seen = []
            while end < len(s) and s[end] not in seen:
                seen.append(s[end])
                end += 1
                ans = max(end - start, ans)
            start += 1
        return ans


print(Solution().lengthOfLongestSubstring("abcabcbb"))
