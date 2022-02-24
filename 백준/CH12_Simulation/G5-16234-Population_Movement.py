from sys import stdin
from collections import deque
from typing import List


# 연합 별로 국가들을 묶어서 리턴
def bfs(n: int, left: int, right: int, land: List[List[int]]) -> List[List[tuple]]:
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    visit = [[False] * n for _ in range(n)]
    res = []

    for i in range(n):
        for j in range(n):

            if visit[i][j]:
                continue

            dq = deque()
            dq.append((i, j, land[i][j]))
            union = [(i, j, land[i][j])]
            visit[i][j] = True

            while dq:
                cy, cx, cp = dq.popleft()

                for k in range(4):
                    ny, nx = cy + dy[k], cx + dx[k]

                    if 0 <= ny < n and 0 <= nx < n and not visit[ny][nx]:
                        # 국경선을 공유하는 나라의 인구 차이가 조건을 만족하는 경우
                        if left <= abs(cp - land[ny][nx]) <= right:
                            visit[ny][nx] = True
                            union.append((ny, nx, land[ny][nx]))
                            dq.append((ny, nx, land[ny][nx]))
            if len(union) > 1:
                res.append(union)

    return res


def main():
    N, L, R = map(int, stdin.readline().split())
    land = [list(map(int, stdin.readline().split())) for _ in range(N)]
    cnt = 0
    while True:
        unions = bfs(N, L, R, land)
        is_done = True
        for union in unions:
            yxp = list(zip(*union))
            moved = sum(yxp[2]) // len(yxp[0])

            for i in range(len(yxp[0])):
                if land[yxp[0][i]][yxp[1][i]] != moved:
                    is_done = False
                    land[yxp[0][i]][yxp[1][i]] = moved

        # 인구수가 변경된 나라가 없는 경우 break
        if is_done:
            break
        cnt += 1

    print(cnt)


if __name__ == "__main__":
    main()
