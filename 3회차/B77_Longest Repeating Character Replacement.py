class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def check(target: str, start: int):
            cnt, chance = 0, k
            for letter in s[start:]:
                if letter == target:
                    cnt += 1
                elif chance > 0:
                    cnt += 1
                    chance -= 1
                else:
                    return cnt
            return cnt

        letter_set = set(s)
        result = 0
        for target in letter_set:
            for i in range(len(s)):
                if i > 0 and s[i] == target and s[i] == s[i - 1]:
                    continue
                result = max(result, check(target, i))
        return result


print(Solution().characterReplacement("ABAA",
0))