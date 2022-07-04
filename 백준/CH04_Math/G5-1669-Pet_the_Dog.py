"""
시간 초과
"""
from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 9)


def dfs(cur: int, h: int, day: int):
    global ans

    if day >= ans - 1 or cur > y:
        return
    elif cur == y - 1:
        ans = min(day + 1, ans)
        return

    dfs(cur + h + 1, h + 1, day + 1)
    dfs(cur + h, h, day + 1)
    if h > 1:
        dfs(cur + h - 1, h - 1, day + 1)


if __name__ == "__main__":
    x, y = map(int, stdin.readline().rstrip().split())

    if y - x == 1:
        print(1)
        exit()

    ans = 2 ** 31 + 1
    dfs(x + 1, 1, 1)
    print(ans)
