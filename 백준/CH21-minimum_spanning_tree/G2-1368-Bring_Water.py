from sys import stdin
input = lambda: stdin.readline().rstrip()


def find(x: int) -> int:
    if parents[x] < 0:
        return x
    parents[x] = find(parents[x])
    return parents[x]


def union(x: int, y: int) -> None:
    x, y = find(x), find(y)
    parents[x] += parents[y]
    parents[y] = x


def mst() -> int:
    costs = [[W[i], 0, i + 1] for i in range(N)]
    for i in range(N):
        for j in range(i + 1, N):
            costs.append([P[i][j], i + 1, j + 1])

    costs.sort()
    res = 0
    for cost, a, b in costs:
        a, b = find(a), find(b)
        if a != b:
            union(a, b)
            res += cost
            if parents[0] == -(N + 1):
                return res

    return res


if __name__ == "__main__":
    N = int(input())
    W = [int(input()) for _ in range(N)]
    P = [list(map(int, input().split())) for _ in range(N)]

    parents = [-1] * (N + 1)
    print(mst())
