from collections import deque, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def check() -> bool:
            for i in cnt:
                if cnt[i] < 0:
                    return False
            return True

        if not s or not t:
            return ""
        max_str = 'a' * 10 ** 5
        res = max_str
        start, end = 0, 0
        window = deque()
        cnt = defaultdict(int)
        for i in t:
            cnt[i] -= 1

        window.append(s[0])
        cnt[s[0]] += 1

        while True:
            if check():
                if len(res) > len(window):
                    res = ''.join(window)
                start += 1
                cnt[window.popleft()] -= 1

            elif not check():
                end += 1
                if end >= len(s):
                    break
                window.append(s[end])
                cnt[s[end]] += 1
        if res == max_str:
            res = ""
        return res


sol = Solution()
# print(sol.minWindow("ADOBECODEBANC", "ABC"))
print(sol.minWindow("a", "aa"))