from sys import stdin

input = lambda: stdin.readline().rstrip()


def dfs(idx):
    global ans

    if idx == M * N:
        ans += 1
        return

    y, x = idx // M, idx % M

    if not (y > 0 and x > 0 and visit[y - 1][x] and visit[y][x - 1] and visit[y - 1][x - 1]):
        visit[y][x] = True
        dfs(idx + 1)
        visit[y][x] = False

    dfs(idx + 1)


if __name__ == "__main__":
    N, M = map(int, input().split())

    visit = list([False] * M for _ in range(N))
    ans = 0

    dfs(0)
    print(ans)
