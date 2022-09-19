from collections import deque


INF = 2500


def dfs(cur: int, m: int):
    if m == 0:
        bfs(blank_cnt)
        return

    for i in range(cur, len(viruses)):
        check[i] = True
        dfs(i + 1, m - 1)
        check[i] = False


def bfs(cnt: int) -> None:
    global ans

    dq = deque()
    visit = list([False] * N for _ in range(N))

    for i in range(len(viruses)):
        if check[i]:
            y, x = viruses[i][0], viruses[i][1]
            dq.append((y, x, 0, cnt))
            visit[y][x] = True

    while dq:
        cy, cx, move, cc = dq.popleft()
        if cc == 0:
            ans = min(ans, move)
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < N and 0 <= nx < N and not visit[ny][nx] and arr[ny][nx] != 1:
                visit[ny][nx] = True
                if arr[ny][nx] == 0:
                    cnt -= 1
                dq.append((ny, nx, move + 1, cnt))


if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = list(list(map(int, input().split())) for _ in range(N))

    viruses = []
    blank_cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                blank_cnt += 1
            elif arr[i][j] == 2:
                viruses.append((i, j))

    check = [False] * len(viruses)
    ans = INF
    dfs(0, M)
    print([ans, -1][ans == INF])
