from sys import stdin
from typing import List
from collections import deque
input = lambda: stdin.readline().rstrip()


def bfs(sy: int, sx: int, visit: List[List[bool]]) -> List:
    dq = deque([(sy, sx)])
    visit[sy][sx] = True
    blocks = [(sy, sx)]
    total_cnt, rainbow_cnt = 1, 0
    while dq:
        cy, cx = dq.popleft()
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < N and 0 <= nx < N and not visit[ny][nx] and \
                    (arr[ny][nx] == arr[sy][sx] or arr[ny][nx] == 0):
                total_cnt += 1
                visit[ny][nx] = True
                blocks.append((ny, nx))
                dq.append((ny, nx))

    for y, x in blocks:
        if arr[y][x] == 0:
            rainbow_cnt += 1
            visit[y][x] = False

    return [total_cnt, rainbow_cnt, blocks]  # 전체 블록 개수, 무지개 블록 개수, 블록 그룹 좌표


def remove(crds: List) -> None:
    for y, x in crds:
        arr[y][x] = -2


def gravity() -> None:
    for c in range(N):
        for r in range(N - 2, -1, -1):
            for k in range(r, N - 1):
                if arr[k][c] >= 0 and arr[k + 1][c] == -2:
                    arr[k][c], arr[k + 1][c] = -2, arr[k][c]
                else:
                    break


def rotate() -> None:
    global arr
    arr = list(list(i) for i in list(zip(*arr))[::-1])[:]


def autoplay() -> int:
    score = 0
    while True:
        groups = []
        visit = [[False] * N for _ in range(N)]
        for r in range(N):
            for c in range(N):
                if arr[r][c] > 0 and not visit[r][c]:
                    res = bfs(r, c, visit)
                    if res[0] > 1:
                        groups.append([res[0], res[1], (r, c), res[2][:]])

        if not groups:
            break

        groups.sort(reverse=True)
        remove(groups[0][3])
        score += groups[0][0] ** 2
        gravity()
        rotate()
        gravity()

    return score


if __name__ == "__main__":
    N, M = map(int, input().split())  # 격차 크기, 색상 개수
    arr = list(list(map(int, input().split())) for _ in range(N))

    print(autoplay())
