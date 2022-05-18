from sys import stdin
from collections import defaultdict


input = lambda: stdin.readline().rstrip()


if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = [0] + list(map(int, input().split()))

    cnts = defaultdict(int)
    for i in range(1, N + 1):
        arr[i] += arr[i - 1]
        cnts[arr[i] % M] += 1

    ans = cnts[0] * (cnts[0] + 1) >> 1
    for i in range(1, M):
        ans += cnts[i] * (cnts[i] - 1) >> 1
    print(ans)
