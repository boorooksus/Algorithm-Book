from sys import stdin


input = lambda: stdin.readline().rstrip()


def find(x: int) -> int:
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]


def union(x: int, y: int) -> None:
    x, y = find(x), find(y)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y


if __name__ == "__main__":
    T = int(input())
    for i in range(1, T + 1):
        n, k = (int(input()) for _ in range(2))
        parents = list(i for i in range(n))
        for _ in range(k):
            a, b = map(int, input().split())
            union(a, b)
        m = int(input())
        print('Scenario %d:' % i)
        for _ in range(m):
            u, v = map(int, input().split())
            print([0, 1][find(u) == find(v)])
        print()
