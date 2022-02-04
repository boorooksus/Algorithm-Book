from sys import stdin, maxsize


n = k = 0
costs = []


def main():
    def input():
        return stdin.readline().rstrip()

    global n, k, costs

    n = int(input())
    costs = [[0, 0]]
    for _ in range(n - 1):
        costs.append(list(map(int, input().split())))
    k = int(input())

    print(min_cost())


def min_cost() -> int:
    if n < 2:
        return 0
    if n == 2:
        return costs[-1][0]

    dp = list([0] + [costs[1][0]] + [0] * (n - 2) for _ in range(n + 1))

    if n == 3:
        return min(dp[0][1] + costs[2][0], costs[2][1])

    res = maxsize
    for i in range(3, n + 1):
        for j in range(2, n):
            if i != n and i - 2 <= j < i:
                continue
            elif j == i:
                dp[i][j] = dp[i][j - 3] + k
            elif j == i + 1:
                dp[i][j] = dp[i][j - 1] + costs[j][0]
            else:
                sjump = dp[i][j - 1] + costs[j][0]
                ljump = dp[i][j - 2] + costs[j][1]
                dp[i][j] = min(sjump, ljump)

        res = min(dp[i][n - 1], res)

    return res if res < maxsize else costs[-1][0]


if __name__ == "__main__":
    main()


"""
틀림.
문제 입력 조건 잘못 읽음
"""