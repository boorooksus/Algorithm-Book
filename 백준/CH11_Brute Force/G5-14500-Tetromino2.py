from sys import stdin


dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]


def dfs(y, x, cnt, total) -> int:
    total += arr[y][x]

    if cnt == 4:
        return total

    res = 0
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < N and 0 <= nx < M and not visit[ny][nx]:
            visit[ny][nx] = True
            res = max(dfs(ny, nx, cnt + 1, total), res)

            if cnt == 2:
                for j in range(i + 1, 4):
                    my, mx = y + dy[j], x + dx[j]
                    if 0 <= my < N and 0 <= mx < M and not visit[my][mx]:
                        res = max(total + arr[ny][nx] + arr[my][mx], res)

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
            visit[i][j] = True
            ans = max(dfs(i, j, 1, 0), ans)
            visit[i][j] = False

    print(ans)
