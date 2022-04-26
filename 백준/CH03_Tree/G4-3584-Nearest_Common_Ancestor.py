from sys import stdin, setrecursionlimit
from collections import defaultdict
setrecursionlimit(10 ** 9)


def dfs(cur: int, dest: int) -> bool:
    if cur == dest:
        return True

    for child in children[cur]:
        if not visit[child] and dfs(child, dest):
            return True

    return False


def nca(x: int, y: int) -> int:
    parent = x

    while parents[parent]:
        if dfs(parent, y):
            break
        visit[parent] = True
        parent = parents[parent]

    return parent


if __name__ == "__main__":
    def input():
        return stdin.readline().rstrip()

    T = int(input())
    for _ in range(T):
        N = int(input())

        children = defaultdict(list)
        parents = defaultdict(int)
        visit = defaultdict(bool)

        for _ in range(N - 1):
            a, b = map(int, input().split())
            children[a].append(b)
            parents[b] = a
        x, y = map(int, input().split())

        print(nca(x, y))
