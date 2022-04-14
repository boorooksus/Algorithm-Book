"""
시간초과
"""
from sys import stdin
from collections import deque

dy = [1, -1, 0, 1]
dx = [0, 0, 1, -1]


def bfs() -> int:
    visit = list([False] * N for _ in range(N))
    dq = deque()

    for y, line in enumerate(arr):
        if 'S' in line:
            x = line.index('S')
            dq.append((y, x, H, 0, 0))
            visit[y][x] = True
            break

    while dq:
        cy, cx, hp, shield, move = dq.popleft()

        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            nh, ns = hp, shield
            if 0 <= ny < N and 0 <= nx < N \
                    and not visit[ny][nx] and  hp + shield > 0:
                if arr[ny][nx] == 'E':
                    return move + 1

                if ns > 0:
                    ns -= 1
                else:
                    nh -= 1
                if arr[ny][nx] == 'U':
                    ns = D
                dq.append((ny, nx, nh, ns, move + 1))
                visit[ny][nx] = True

    return -1


if __name__ == "__main__":
    def input():
        return stdin.readline().rstrip()


    N, H, D = map(int, input().split())
    arr = [input() for _ in range(N)]

    print(bfs())
