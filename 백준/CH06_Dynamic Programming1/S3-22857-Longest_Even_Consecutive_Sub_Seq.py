from sys import stdin


if __name__ == "__main__":
    def input():
        return stdin.readline().rstrip()

    N, K = map(int, input().split())
    seq = list(map(int, input().split()))

    dp = []
    cnt = 0
    for num in seq:
        if num % 2 == 0:
            cnt += 1
        else:
            dp.append(cnt)
            cnt = 0
    dp.append(cnt)

    if len(dp) <= K + 1:
        print(sum(dp))
    else:
        ans = 0
        for i in range(K + 1):
            ans += dp[i]
        cnt = ans
        for i in range(K + 1, len(dp)):
            cnt += dp[i] - dp[i - K - 1]
            ans = max(cnt, ans)
        print(ans)
