from sys import stdin, maxsize


n = k = 0
costs = []


def main():
    def input():
        return stdin.readline().rstrip()

    global n, k, costs

    n = int(input())
    costs = []
    for _ in range(n - 1):
        costs.append(list(map(int, input().split())))
    k = int(input())

    print(min_cost())


def min_cost() -> int:
    if n == 1:
        return 0
    if n == 2:
        return costs[-1][0]

    temp = min(costs[0][0] + costs[1][0], costs[0][1])

    if n == 3:
        return temp

    dp = list([0] + [costs[0][0]] + [temp] + [0] * (n - 3) for _ in range(n + 1))

    res = maxsize
    for i in range(3, n + 1):
        for j in range(2, n):
            if i != n and i - 2 <= j < i:
                continue
            elif j == i:
                dp[i][j] = dp[i][j - 3] + k
            elif j == i + 1:
                dp[i][j] = dp[i][j - 1] + costs[j - 1][0]
            else:
                sjump = dp[i][j - 1] + costs[j - 1][0]
                ljump = dp[i][j - 2] + costs[j - 2][1]
                dp[i][j] = min(sjump, ljump)

        res = min(dp[i][n - 1], res)

    return res


if __name__ == "__main__":
    main()
