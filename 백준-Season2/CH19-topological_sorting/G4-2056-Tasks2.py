from sys import stdin
from collections import defaultdict
input = lambda: stdin.readline().rstrip()


if __name__ == "__main__":
    N = int(input())

    prevs = defaultdict(list)
    dp = [0] * (N + 1)

    for i in range(1, N + 1):
        x = list(map(int, input().split()))
        dp[i] = x[0]
        for j in range(2, 2 + x[1]):
            prevs[i].append(x[j])

    for i in range(2, N + 1):
        temp = 0
        for prev in prevs[i]:
            temp = max(temp, dp[prev])
        dp[i] += temp

    print(max(dp))


"""
다이나믹 프로그래밍 이용한 방식
"""
