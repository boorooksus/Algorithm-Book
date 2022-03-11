from sys import stdin
from typing import List
from itertools import combinations


lab, viruses, blanks = [], [], []
n, m = 0, 0
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]


def dfs(y: int, x: int, lab_copy: List[List[int]]) -> None:
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < n and 0 <= nx < m and lab_copy[ny][nx] == 0:
            lab_copy[ny][nx] = 2
            dfs(ny, nx, lab_copy)


def main():
    def input():
        return stdin.readline().rstrip()
    global lab, viruses, n, m

    n, m = map(int, input().split())
    lab = [list(map(int, input().split())) for _ in range(n)]

    # 바이러스, 빈 공간 위치 저장
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 2:
                viruses.append((i, j))
            elif lab[i][j] == 0:
                blanks.append((i, j))

    res = 0
    # 벽 세우기
    combs = combinations(blanks, 3)
    for comb in combs:
        lab_copy = [row[:] for row in lab]
        for y, x in comb:
            lab_copy[y][x] = 1
        # 벽 3개 다 세우면 바이러스 확산
        for y, x in viruses:
            dfs(y, x, lab_copy)
        # 안전 지대 개수 구하기
        safezone = sum(i.count(0) for i in lab_copy)
        res = max(safezone, res)

    print(res)


if __name__ == "__main__":
    main()
