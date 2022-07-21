class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        used = {}
        result = start = 0

        for index, char in enumerate(s):
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:
                result = max(result, index - start + 1)

            used[char] = index

        return result


print(Solution().lengthOfLongestSubstring("au"))