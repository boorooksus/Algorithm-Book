"""
문제 조건 잘못 읽음
테트로미노를 하나만 넣도록 바꿔야함
"""
from sys import stdin


dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]


def dfs(y, x, cnt, total, route):
    total += arr[y][x]

    if cnt == 4:
        return total, route

    res = [0, []]
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < N and 0 <= nx < M and not visit[ny][nx]:
            visit[ny][nx] = True
            temp = dfs(ny, nx, cnt + 1, total, route + [(ny, nx)])
            if temp[0] > res[0]:
                res = [temp[0], temp[1][:]]
            visit[ny][nx] = False

    return res


if __name__ == "__main__":
    input = lambda: stdin.readline().rstrip()

    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visit = list([False] * M for _ in range(N))
    ans = 0
    for i in range(N):
        for j in range(M):
            if not visit[i][j]:
                visit[i][j] = True
                temp = dfs(i, j, 0, 0, [])
                ans += temp[0]
                for y, x in temp[1]:
                    visit[y][x] = True

    print(ans)
