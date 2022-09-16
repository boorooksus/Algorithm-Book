INF = 1000000


def dfs(cur: int, cnt: int) -> None:
    if not cnt:
        cal()
        return

    for i in range(cur, len(chickens) - cnt + 1):
        visit[i] = True
        dfs(i + 1, cnt - 1)
        visit[i] = False


def cal() -> None:
    global ans

    total = 0
    for home in range(len(homes)):
        for dist, chicken in dists[home]:
            if visit[chicken]:
                total += dist
                break

    ans = min(total, ans)


if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = list(list(map(int, input().split())) for _ in range(N))

    homes, chickens = [], []
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 1:
                homes.append((r, c))
            elif arr[r][c] == 2:
                chickens.append((r, c))

    dists = {i: [] for i in range(len(homes))}
    for home in range(len(homes)):
        for chicken in range(len(chickens)):
            dists[home].append((abs(homes[home][0] - chickens[chicken][0]) \
                                + abs(homes[home][1] - chickens[chicken][1]), chicken))
        temp = dists[home][:]
        dists[home] = sorted(temp)

    visit = [False] * len(chickens)
    ans = INF
    for i in range(len(chickens) - M + 1):
        visit[i] = True
        dfs(i + 1, M - 1)
        visit[i] = False
    print(ans)
