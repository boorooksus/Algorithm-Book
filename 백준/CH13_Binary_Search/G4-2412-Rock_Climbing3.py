"""
bfs 이용한 풀이
"""
from sys import stdin
from collections import deque, defaultdict


input = lambda: stdin.readline().rstrip()
INF = 50002


def bfs() -> int:
    dq = deque([(0, 0, 0)])
    while dq:
        x, y, cnt = dq.popleft()

        if y == T:
            return cnt

        for i in range(x - 2, x + 3):
            for j in range(y - 2, y + 3):
                if x < 0 or y < 0:
                    continue
                if j in crds[i]:
                    dq.append((i, j, cnt + 1))
                    crds[i].remove(j)

    return -1


if __name__ == "__main__":
    n, T = map(int, input().split())
    crds = defaultdict(list)
    for _ in range(n):
        x, y = map(int, input().split())
        crds[x].append(y)

    print(bfs())
