class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        ans, start = 0, 0
        for i, char in enumerate(s):
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:
                ans = max(i - start + 1, ans)

            used[char] = i

        return ans


print(Solution().lengthOfLongestSubstring("abcabcbb"))
