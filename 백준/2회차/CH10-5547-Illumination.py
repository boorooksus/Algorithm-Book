from sys import stdin
from collections import deque

input = lambda: stdin.readline().rstrip()


def bfs() -> int:
    even_move = [(1, 0), (1, -1), (-1, 0), (-1, -1), (0, 1), (0, -1)]
    odd_move = [(1, 0), (1, 1), (-1, 0), (-1, 1), (0, 1), (0, -1)]

    visit = list([False] * (W + 2) for _ in range(H + 2))
    dq = deque([(0, 0)])
    visit[0][0] = True
    cnt = 0

    while dq:
        cy, cx = dq.popleft()
        for dy, dx in [even_move, odd_move][cy % 2 == 1]:
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < H + 2 and 0 <= nx < W + 2:
                if arr[ny][nx] == 1:
                    cnt += 1
                elif not visit[ny][nx]:
                    visit[ny][nx] = True
                    dq.append((ny, nx))

    return cnt


if __name__ == "__main__":
    W, H = map(int, input().split())
    arr = [list(0 for _ in range(W + 2))] + \
        list([0] + list(map(int, input().split())) + [0] for _ in range(H)) + \
        [list(0 for _ in range(W + 2))]

    print(bfs())
