from sys import stdin
from collections import deque


MAX = 100001


def bfs() -> int:
    times = [-1] * MAX
    dq = deque([n])
    times[n] = 0

    while dq:
        cur = dq.popleft()

        if cur == k:
            return times[cur]

        if 2 * cur < MAX and times[2 * cur] == -1:
            times[2 * cur] = times[cur]
            dq.appendleft(2 * cur)
        if cur - 1 >= 0 and times[cur - 1] == -1:
            times[cur - 1] = times[cur] + 1
            dq.append(cur - 1)
        if cur + 1 < MAX and times[cur + 1] == -1:
            times[cur + 1] = times[cur] + 1
            dq.append(cur + 1)

    return 0


if __name__ == "__main__":
    n, k = map(int, stdin.readline().split())

    print(bfs())

