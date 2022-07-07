from sys import stdin


input = lambda: stdin.readline().rstrip()
INF = 10001


if __name__ == "__main__":
    N, M = map(int, input().split())
    pans = list(map(int, input().split()))

    dp = [0] + [INF] * N
    for i in range(1, N + 1):
        for j in range(M):
            pan = pans[j]
            if pan > i:
                continue
            if dp[i - pan] != INF:
                dp[i] = min(dp[i - pan] + 1, dp[i])
            for k in range(j + 1, M):
                pan2 = pans[k]
                if pan + pan2 > i or dp[i - pan - pan2] == INF:
                    continue
                dp[i] = min(dp[i - pan - pan2] + 1, dp[i])

    print([dp[N], -1][dp[N] == INF])
