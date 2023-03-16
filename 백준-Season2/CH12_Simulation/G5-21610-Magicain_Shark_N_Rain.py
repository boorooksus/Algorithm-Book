from sys import stdin
from collections import deque
from typing import List, Tuple
input = lambda: stdin.readline().rstrip()


def move(d: int, s: int, idx: int) -> List[Tuple[int, int]]:
    dy = [0, -1, -1, -1, 0, 1, 1, 1]
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]

    res = []
    while clouds:
        y, x = clouds.popleft()
        # 1. move
        ny, nx = (y + dy[d] * s) % N, (x + dx[d] * s) % N

        # 2. add water in basket
        arr[ny][nx] += 1

        # 3. disappear and remark the clouds
        visit[ny][nx] = idx
        res.append((ny, nx))

    return res


def magic(locs: List[Tuple[int, int]], idx: int) -> None:
    dy = [-1, -1, 1, 1]
    dx = [-1, 1, 1, -1]

    # 4. duplicating water magic
    for y, x in locs:
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < N and arr[ny][nx] > 0:
                arr[y][x] += 1

    # 5. make clouds
    for y in range(N):
        for x in range(N):
            if arr[y][x] >= 2 and visit[y][x] != idx:
                clouds.append((y, x))
                arr[y][x] -= 2


if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    clouds = deque([(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)])
    visit = [[0] * N for _ in range(N)]

    for i in range(1, M + 1):
        d, s = map(int, input().split())
        res = move(d - 1, s, i)
        magic(res, i)

    print(sum(sum(arr[i]) for i in range(N)))
