from sys import stdin
input = lambda: stdin.readline().rstrip()
INF = 4000


def cal() -> None:
    global ans

    score = [0, 0]
    for i in range(N):
        for j in range(i + 1, N):
            if team[i] == team[j]:
                score[team[i]] += S[i][j]

    ans = min(ans, abs(score[0] - score[1]))


def dfs(cur: int) -> None:
    cal()

    for i in range(cur, N):
        team[i] = 1
        dfs(i + 1)
        team[i] = 0


if __name__ == "__main__":
    N = int(input())
    S = list(list(map(int, input().split())) for _ in range(N))

    for i in range(N):
        for j in range(i + 1, N):
            S[i][j] += S[j][i]

    team = [0] * N
    ans = INF
    dfs(0)
    print(ans)
