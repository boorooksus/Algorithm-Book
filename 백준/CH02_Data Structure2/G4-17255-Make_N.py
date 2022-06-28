"""
숫자를 붙여나가는 방식
"""
from sys import stdin


def dfs(route: str, sidx: int, eidx: int) -> None:
    if len(route) == target:
        ans.add(route)
        return

    if sidx > 0:
        dfs(route + x[sidx - 1: eidx + 1], sidx - 1, eidx)
    if eidx < len(x):
        dfs(route + x[sidx: eidx + 2], sidx, eidx + 1)


if __name__ == "__main__":
    x = stdin.readline().rstrip()

    ans = set()
    target = len(x) * (len(x) + 1) // 2
    for i, v in enumerate(x):
        dfs(v, i, i)

    print(len(ans))

