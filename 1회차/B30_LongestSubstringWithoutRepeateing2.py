class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = max_len = 0
        used = {}

        for idx, char in enumerate(s):
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:
                max_len = max(max_len, idx - start + 1)

            used[char] = idx

        return max_len


sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))
