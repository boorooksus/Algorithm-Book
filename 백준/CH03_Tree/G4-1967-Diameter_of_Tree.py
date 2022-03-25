from sys import stdin, setrecursionlimit
from collections import defaultdict
setrecursionlimit(10 ** 9)


tree = defaultdict(list)
res = 0


def dfs(node: int) -> int:
    global res

    if not tree[node]:
        return 0

    radii = []
    for child, weight in tree[node]:
        radii.append(weight + dfs(child))
    if len(radii) > 2:
        radii.sort(reverse=True)
        res = max(radii[0] + radii[1], res)
    else:
        res = max(sum(radii), res)
    return max(radii)


def main():
    def input():
        return stdin.readline().rstrip()

    n = int(input())
    for _ in range(n - 1):
        p, c, w = map(int, input().split())
        tree[p].append((c, w))

    dfs(1)
    print(res)


if __name__ == "__main__":
    main()