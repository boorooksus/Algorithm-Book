from sys import stdin


input = lambda: stdin.readline().rstrip()


if __name__ == "__main__":
    N = int(input())
    tasks = list(list(map(int, input().split())) for _ in range(N))

    dp = [0] * (N + 1)
    for start in range(N):
        if start > 1:
            dp[start] = max(dp[start - 1], dp[start])
        end = start + tasks[start][0]
        if end <= N:
            dp[end] = max(dp[start] + tasks[start][1], dp[end])

    print(max(dp))
