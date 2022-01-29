import sys
sys.setrecursionlimit(10 ** 9)

n = 0
parents = []


def get_parent(x: int) -> int:
    if parents[x] == x:
        return x
    else:
        parents[x] = get_parent(parents[x])
        return parents[x]


def union_parent(x: int, y: int) -> None:
    px, py = get_parent(x), get_parent(y)

    if px < py:
        parents[py] = px
    else:
        parents[px] = py


def main():
    def input():
        return sys.stdin.readline().strip()

    global n, parents

    n, m = map(int, input().split())
    for i in range(n + 1):
        parents.append(i)

    for _ in range(m):
        cmd, a, b = map(int, input().split())

        if cmd == 0:
            union_parent(a, b)

        elif cmd == 1:
            if get_parent(a) == get_parent(b):
                print('YES')
            else:
                print('NO')


if __name__ == "__main__":
    main()