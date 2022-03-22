"""
그리디 알고리즘
시간초과
"""
from sys import stdin


def main():
    def input():
        return stdin.readline().rstrip()

    g = int(input())
    p = int(input())
    planes = [int(input()) for _ in range(p)]

    res = 0
    gates = [False] * (g + 1)
    for plane in planes:
        while plane > 0 and gates[plane]:
            plane -= 1

        if plane == 0:
            break
        gates[plane] = True
        res += 1

    print(res)


if __name__ == "__main__":
    main()
