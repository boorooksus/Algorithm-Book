"""
속도 개선
참고: https://velog.io/@jajubal/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EB%B0%B1%EC%A4%80-14500-%ED%85%8C%ED%8A%B8%EB%A1%9C%EB%AF%B8%EB%85%B8
"""
from sys import stdin


dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]


def dfs(y, x, cnt, total) -> None:
    global ans

    total += arr[y][x]

    if ans >= total + max_val * (4 - cnt):
        return

    if cnt == 4:
        ans = max(total, ans)
        return

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < N and 0 <= nx < M and not visit[ny][nx]:
            visit[ny][nx] = True
            dfs(ny, nx, cnt + 1, total)

            if cnt == 2:
                for j in range(i + 1, 4):
                    my, mx = y + dy[j], x + dx[j]
                    if 0 <= my < N and 0 <= mx < M and not visit[my][mx]:
                        ans = max(total + arr[ny][nx] + arr[my][mx], ans)

            visit[ny][nx] = False


if __name__ == "__main__":
    input = lambda: stdin.readline().rstrip()

    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visit = list([False] * M for _ in range(N))
    ans, max_val = 0, max(map(max, arr))
    for i in range(N):
        for j in range(M):
            visit[i][j] = True
            dfs(i, j, 1, 0)
            visit[i][j] = False

    print(ans)
