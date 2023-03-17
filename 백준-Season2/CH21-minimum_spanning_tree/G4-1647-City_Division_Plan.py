from sys import stdin
input = lambda: stdin.readline().rstrip()


def find(x: int) -> int:
    if parents[x] < 0:
        return x
    parents[x] = find(parents[x])
    return parents[x]


def union(x: int, y: int) -> None:
    x, y = find(x), find(y)
    if x < y:
        parents[x] += parents[y]
        parents[y] = x
    else:
        parents[y] += parents[x]
        parents[x] = y


def kruscal() -> int:
    dists.sort()
    res = 0

    for dist, a, b in dists:
        a, b = find(a), find(b)

        if a != b:
            union(a, b)
            res += dist

            if parents[find(a)] == -N:
                return res - dist

    return res


if __name__ == "__main__":
    N, M = map(int, input().split())
    dists = []
    parents = [-1] * (N + 1)

    for _ in range(M):
        a, b, c = map(int, input().split())
        dists.append((c, a, b))

    print(kruscal())
