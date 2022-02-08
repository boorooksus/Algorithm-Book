"""
비트 연산
"""

from sys import stdin


def main():
    def input():
        return stdin.readline().rstrip()

    n = int(input())
    ings = []
    for _ in range(n):
        s, b = map(int, input().split())
        ings.append((s, b))

    res = 2e9
    for i in range(1, 1 << n):
        ts, tb = 1, 0
        for j in range(n):
            if i & 1 << j:
                ts *= ings[j][0]
                tb += ings[j][1]

        res = min(abs(ts - tb), res)

    print(res)


if __name__ == "__main__":
    main()
