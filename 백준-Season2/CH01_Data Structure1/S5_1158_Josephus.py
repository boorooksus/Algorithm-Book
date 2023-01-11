from sys import stdin
from collections import deque


input = stdin.readline().rstrip()


if __name__ == "__main__":
    N, K = map(int, input.split())

    dq = deque(i for i in range(1, N + 1))
    ans = []
    while dq:
        dq.rotate(-K + 1)
        ans.append(dq.popleft())

    print('<', end='')
    print(*ans, sep=', ', end='')
    print('>')
