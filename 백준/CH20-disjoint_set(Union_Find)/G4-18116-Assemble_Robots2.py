from sys import stdin


parents = [-1] * 1000001


def find(x: int) -> int:
    if parents[x] < 0:
        return x

    parents[x] = find(parents[x])
    return parents[x]


def union(x: int, y: int) -> None:
    x, y = find(x), find(y)
    if x == y:
        return
    if x < y:
        parents[x] += parents[y]
        parents[y] = x
    else:
        parents[y] += parents[x]
        parents[x] = y


def main():
    n = int(stdin.readline())
    for _ in range(n):
        cmd = list(map(str, stdin.readline().strip().split()))
        if cmd[0] == 'I':
            union(int(cmd[1]), int(cmd[2]))
        else:
            print(parents[find(int(cmd[1]))] * -1)


if __name__ == "__main__":
    main()
