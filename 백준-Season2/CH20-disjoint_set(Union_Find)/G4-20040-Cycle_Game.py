from sys import stdin
input = lambda: stdin.readline().rstrip()


def find(x: int) -> int:
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]


def union(x: int, y: int) -> bool:
    x, y = find(x), find(y)
    if x == y:
        return False
    if x < y:
        parents[y] = x
    else:
        parents[x] = y
    return True


if __name__ == "__main__":
    n, m = map(int, input().split())

    parents = [i for i in range(n)]

    res = 0
    for i in range(1, m + 1):
        a, b = map(int, input().split())
        if res == 0 and not union(a, b):
            res = i
    print(res)
