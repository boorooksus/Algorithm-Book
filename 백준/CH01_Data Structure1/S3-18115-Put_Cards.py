from sys import stdin
from collections import deque


input = lambda: stdin.readline().rstrip()


if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))

    dq = deque()
    for i, skill in enumerate(arr[::-1], 1):
        if skill == 1:
            dq.appendleft(i)
        elif skill == 2:
            dq.insert(1, i)
        else:
            dq.append(i)

    print(*dq)
