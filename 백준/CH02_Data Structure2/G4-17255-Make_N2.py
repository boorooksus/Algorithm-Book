"""
숫자를 지워 나가는 방식
"""
from sys import stdin


def dfs(num: str) -> None:
    global ans

    if len(set(num)) == 1:
        ans += 1
        return

    dfs(num[1:])
    dfs(num[:-1])


if __name__ == "__main__":
    x = stdin.readline().rstrip()
    ans = 0
    dfs(x)
    print(ans)
