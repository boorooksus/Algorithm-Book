"""
틀림
"""

from collections import deque
from typing import List


def catch_fish(y: int, x: int) -> List:
    res = []
    for r, c, _ in fishes:
        if (y, x) == (r, c):
            res.append((r, c))
    return res


def eat_fishes(caught_fishes: List, cur: int) -> deque:
    res = deque()
    for y, x, d in fishes:
        for r, c in caught_fishes:
            if (y, x) == (r, c):
                smells[r][c] = cur
                break
        else:
            res.append((y, x, d))
    return res


def dfs(cy: int, cx: int, cur: int, visit: List[List[bool]]) -> (List, List):
    shark_move = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    if cur == 3:
        return catch_fish(cy, cx), [(cy, cx)]

    max_cnt, max_caught, max_path = -1, [], []
    for dy, dx in shark_move:
        ny, nx = cy + dy, cx + dx
        if 0 <= ny < 4 and 0 <= nx < 4 and not visit[ny][nx]:
            visit[ny][nx] = True
            caught, path = dfs(ny, nx, cur + 1, visit)
            if len(caught) > max_cnt:
                max_cnt = len(caught)
                max_caught = caught
                max_path = [(cy, cx)] + path
            visit[ny][nx] = False

    return catch_fish(cy, cx) + max_caught, max_path


def copy(cur: int) -> None:
    global fishes, shark
    fish_move = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

    # 1: 복제 시작
    progress = []

    # 2: 물고기가 한 칸씩 이동
    l = len(fishes)
    for _ in range(l):
        cy, cx, d = fishes.popleft()
        progress.append((cy, cx, d))
        for i in range(len(fish_move)):
            nd = (d - i) % len(fish_move)
            ny, nx = cy + fish_move[nd][0], cx + fish_move[nd][1]
            if 0 <= ny < 4 and 0 <= nx < 4 and (ny, nx) != shark and smells[ny][nx] + 2 < cur:
                fishes.append((ny, nx, nd))
                break
        else:
            # 이동할 수 있는 칸이 없는 경우
            fishes.append((cy, cx, d))

    # 3: 상어가 3칸 이동
    visit = list([False] * 4 for _ in range(4))
    visit[shark[0]][shark[1]] = True
    caught_fishes, path = dfs(shark[0], shark[1], 0, visit)
    fishes = eat_fishes(caught_fishes, cur)
    shark = path[-1]

    # 5: 복제 마법 완료
    fishes += progress


if __name__ == "__main__":
    M, S = map(int, input().split())
    fishes = deque()
    for i in range(1, M + 1):
        a, b, d = map(int, input().split())
        fishes.append((a - 1, b - 1, d - 1))  # row, col, dir
    a, b = map(int, input().split())
    shark = (a - 1, b - 1)
    smells = [[-2] * 4 for _ in range(4)]

    for i in range(1, S + 1):
        copy(i)

    print(len(fishes))
