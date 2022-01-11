class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        used = {}
        start = 0

        for i, char in enumerate(s):
            if s[i] in used and start <= used[char]:
                start = used[char] + 1
            else:
                res = max(res, i - start + 1)
            used[char] = i

        return res


print(Solution().lengthOfLongestSubstring("abcabcbb"))