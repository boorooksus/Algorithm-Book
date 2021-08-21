from collections import Counter


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        counts = Counter()
        result = 0

        def check():
            if counts.most_common(1)[0][1] > 1:
                return False
            return True

        start = 0

        for end in range(1, len(s) + 1):
            counts[s[end - 1]] += 1
            while not check():
                counts[s[start]] -= 1
                counts += Counter()
                start += 1
            result = max(result, end - start)

        return result


print(Solution().lengthOfLongestSubstring("au"))
