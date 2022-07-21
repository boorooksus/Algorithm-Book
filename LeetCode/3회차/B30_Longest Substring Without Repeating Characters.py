from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        counts = defaultdict(int)
        result = 0

        def check():
            for v in counts.values():
                if v > 1:
                    return False
            return True

        start = 0

        for end in range(1, len(s) + 1):
            counts[s[end - 1]] += 1
            while not check():
                counts[s[start]] -= 1
                start += 1
            result = max(result, end - start)

        return result


print(Solution().lengthOfLongestSubstring("au"))