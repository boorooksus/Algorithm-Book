"""
유니온파인드
"""
from sys import stdin


parents = []


def find(x: int) -> int:
    if x == parents[x]:
        return x
    parents[x] = find(parents[x])
    return parents[x]


def union(x: int) -> bool:
    x = find(x)
    if x == 0:
        return False
    parents[x] = find(x - 1)
    return True


def main():
    def input():
        return stdin.readline().rstrip()
    global parents

    g = int(input())
    p = int(input())
    planes = [int(input()) for _ in range(p)]

    parents = list(i for i in range(g + 1))
    cnt = 0
    for plane in planes:
        if not union(plane):
            break
        cnt += 1

    print(cnt)


if __name__ == "__main__":
    main()
