from sys import stdin


n = k = 0
costs = []


def main():
    def input():
        return stdin.readline().rstrip()

    global n, k, costs

    n = int(input())
    costs = []

    for i in range(n - 1):
        a, b = map(int, input().split())
        costs.append((a, b))

    k = int(input())

    print(min_cost())


def min_cost() -> int:
    dp = [1e9] * n
    dp[0] = 0

    # 작은 점프, 큰 점프만 이용한 최솟값 찾기
    for i in range(n - 1):
        if i + 1 < n:
            dp[i + 1] = min(dp[i + 1], dp[i] + costs[i][0])
        if i + 2 < n:
            dp[i + 2] = min(dp[i + 2], dp[i] + costs[i][1])

    # 매우 큰 점프를 포함한 최솟값 찾기
    res = dp[-1]
    for i in range(3, n):
        temp, sjump, ljump = dp[i - 3] + k, 1e9, 1e9
        for j in range(i, n - 1):
            if j + 1 <= n:
                sjump = min(temp + costs[j][0], sjump)
            if j + 2 <= n:
                ljump = min(temp + costs[j][1], ljump)
            temp, sjump, ljump = sjump, ljump, 1e9

        res = min(temp, res)

    return res


if __name__ == "__main__":
    main()
