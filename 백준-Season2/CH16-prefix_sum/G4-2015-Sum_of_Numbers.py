from sys import stdin
from collections import defaultdict
input = lambda: stdin.readline().rstrip()


if __name__ == "__main__":
    N, K = map(int, input().split())
    arr = [0] + list(map(int, input().split()))

    counts = defaultdict(int)
    counts[0] += 1
    ans = 0

    for i in range(1, N + 1):
        arr[i] += arr[i - 1]
        ans += counts[arr[i] - K]
        counts[arr[i]] += 1
    print(ans)
