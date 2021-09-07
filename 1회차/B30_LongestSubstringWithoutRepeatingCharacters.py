from collections import defaultdict, Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        start = end = ans = 0
        while end < len(s):
            freq = Counter(s[start: end + 1])
            check = True
            for i in freq:
                if freq[i] > 1:
                    start += 1
                    check = False
                    break
            if check:
                if ans < end - start + 1:
                    ans = end - start + 1
                end += 1

        return ans


sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))

# leetcode: 3

