from sys import stdin
input = lambda: stdin.readline().rstrip()


MAX = 100_001


if __name__ == "__main__":
    C, N = map(int, input().split())
    costs = list(tuple(map(int, input().split())) for _ in range(N))

    dp = [0] + [MAX] * C
    for i in range(C):
        for cost, client in costs:
            if i + client < C:
                # 늘어나는 고객 수에 따른 최소 비용 비교
                dp[i + client] = min(dp[i + client], dp[i] + cost)
            elif i + client >= C:
                # 늘어나는 고객 수가 C이상일 때 최소 비용 비교
                dp[C] = min(dp[C], dp[i] + cost)

    print(dp[C])

"""
다이나믹 프로그래밍
"""