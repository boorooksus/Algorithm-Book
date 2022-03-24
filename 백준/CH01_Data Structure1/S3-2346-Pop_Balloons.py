from sys import stdin
from collections import deque


def main():
    def input():
        return stdin.readline().rstrip()

    n = int(input())
    balloons = list(map(int, input().split()))

    dq = deque(list((i + 1, -balloons[i]) for i in range(n)))
    res = []
    while dq:
        idx, move = dq.popleft()
        if move < 0:
            move += 1
        res.append(idx)
        dq.rotate(move)

    print(*res, sep=' ')


if __name__ == "__main__":
    main()

