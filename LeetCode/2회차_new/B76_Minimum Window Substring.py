from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        left = start = end = 0
        missing = len(t)

        # == 1 ================================
        for right, char in enumerate(s, 1):
            missing -= need[char] > 0
            need[char] -= 1

            if missing == 0:
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1

                if not end or right - left <= end - start:
                    start, end = left, right
                need[s[left]] += 1
                missing += 1
                left += 1

        return s[start:end]

print(Solution().minWindow("ADOBECODEBANC",
"ABC"))

# 1: char는 맨 처음부터 시작하지만, 인덱스는 1부터 시작
#    right는 마지막 문자 인덱스가 아닌 +1한 값
