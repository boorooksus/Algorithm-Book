"""
출력초과(메모리초과)
"""

from sys import stdin, stdout
from collections import defaultdict


parents = defaultdict(int)
dp = defaultdict(int)


def get_parent(x: int) -> int:
    global parents, dp
    if not parents[x] or parents[x] == x:
        parents[x] = x
        return x

    parents[x] = get_parent(parents[x])
    return parents[x]


def union_parent(x: int, y: int) -> None:
    global parents, dp
    x, y = get_parent(x), get_parent(y)
    dp[x], dp[y] = count_parts(x), count_parts(y)
    if x < y:
        parents[y] = x
        dp[x] += dp[y]
    else:
        parents[x] = y
        dp[y] += dp[x]


def count_parts(x: int) -> int:
    global parents, dp
    x = get_parent(x)
    if not dp[x]:
        dp[x] = 1

    return dp[x]


def main():
    global parents, dp
    n = int(stdin.readline())
    for _ in range(n):
        cmd = list(stdin.readline().strip().split())
        if cmd[0] == 'I':
            union_parent(int(cmd[1]), int(cmd[2]))
        else:
            stdout.write(str(count_parts(int(cmd[1]))) + '\n')
            # print(count_parts(int(cmd[1])))


if __name__ == "__main__":
    main()
