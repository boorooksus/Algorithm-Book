from sys import stdin


parents = []


def get_parent(x: int) -> int:
    global parents

    if parents[x] == x:
        return x
    parents[x] = get_parent(parents[x])
    return parents[x]


def union_parent(x: int, y: int) -> None:
    global parents

    x, y = get_parent(x), get_parent(y)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y


def main():
    def input():
        return stdin.readline()
    global parents

    n = int(input())
    m = int(input())
    parents = [i for i in range(n + 1)]
    graph = [[0] * (n + 1)] + \
            [[0] + list(map(int, input().split())) for _ in range(n)]

    places = list(map(int, input().split()))

    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if graph[i][j]:
                union_parent(i, j)

    ans = set([get_parent(place) for place in places])

    if len(ans) == 1:
        print('YES')
    else:
        print('NO')


if __name__ == "__main__":
    main()
