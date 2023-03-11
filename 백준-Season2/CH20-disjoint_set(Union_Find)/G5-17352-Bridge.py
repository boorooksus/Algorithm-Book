from sys import stdin
input = lambda: stdin.readline().rstrip()


def find(x: int) -> int:
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]


def union(x: int, y: int) -> None:
    x, y = find(parents[x]), find(parents[y])
    if x < y:
        parents[y] = x
    else:
        parents[x] = y


if __name__ == "__main__":
    N = int(input())

    parents = [i for i in range(N + 1)]
    for _ in range(N - 2):
        a, b = map(int, input().split())
        union(a, b)

    for i in range(1, N):
        if find(i) != find(i + 1):
            print(i, i + 1)
            break
