from sys import stdin
from copy import deepcopy
from typing import List


lab, viruses = [], []
n, m, res = 0, 0, 0
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]


def select_walls(start: int, cnt: int) -> None:
    global res

    # 벽 3개 모두 세우면 바이러스 확산 후 안전 지대 탐색
    if cnt == 3:
        lab_copy = deepcopy(lab)
        for y, x in viruses:
            dfs(y, x, lab_copy)
        safezone = sum(i.count(0) for i in lab_copy)
        res = max(safezone, res)
        return

    for i in range(start, n * m):
        y, x = i // m, i % m
        if lab[y][x] == 0:
            lab[y][x] = 1
            select_walls(i, cnt + 1)
            lab[y][x] = 0


def dfs(y: int, x: int, lab_copy: List[List[int]]) -> None:
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < n and 0 <= nx < m and lab_copy[ny][nx] == 0:
            lab_copy[ny][nx] = 2
            dfs(ny, nx, lab_copy)


def cnt_safezone(lab_copy: List[List[int]]) -> int:
    cnt = 0
    for i in range(n):
        for j in range(m):
            if lab_copy[i][j] == 0:
                cnt += 1
    return cnt


def main():
    def input():
        return stdin.readline().rstrip()
    global lab, viruses, n, m

    n, m = map(int, input().split())
    lab = [list(map(int, input().split())) for _ in range(n)]

    # 바이러스 위치 저장
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 2:
                viruses.append((i, j))

    # 벽 세우기
    select_walls(0, 0)

    print(res)


if __name__ == "__main__":
    main()



