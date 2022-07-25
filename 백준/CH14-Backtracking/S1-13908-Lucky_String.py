from sys import stdin
from collections import Counter


def dfs(cur: str):
    global res

    if len(cur) == len(s):
        res += 1

    for char in cnt.keys():
        if not cur or (cnt[char] > 0 and cur[-1] != char):
            cnt[char] -= 1
            dfs(cur + char)
            cnt[char] += 1


s = list(stdin.readline().rstrip())
cnt = Counter(s)
res = 0
dfs('')
print(res)
