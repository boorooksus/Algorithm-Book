from sys import stdin
input = lambda: stdin.readline().rstrip()


def dfs(player: int, total: int) -> None:
    global ans

    if player == 11:
        ans = max(ans, total)
        return

    for i in range(11):
        if not visit[i] and stats[player][i] > 0:
            visit[i] = True
            dfs(player + 1, total + stats[player][i])
            visit[i] = False


if __name__ == "__main__":
    C = int(input())
    for _ in range(C):
        stats = [list(map(int, input().split())) for _ in range(11)]

        ans = 0
        visit = [False] * 11
        dfs(0, 0)
        print(ans)
