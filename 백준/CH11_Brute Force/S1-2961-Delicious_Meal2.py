from sys import stdin
from itertools import combinations


def main():
    def input():
        return stdin.readline().rstrip()

    n = int(input())
    ings = []
    for _ in range(n):
        s, b = map(int, input().split())
        ings.append((s, b))

    combs = []
    for i in range(1, n + 1):
        combs.append(combinations(ings, i))

    res = 2e9
    for comb in combs:
        for each in comb:
            sour, bitter = 1, 0
            for s, b in each:
                sour *= s
                bitter += b
            res = min(abs(sour - bitter), res)

    print(res)


if __name__ == "__main__":
    main()
