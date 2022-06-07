from sys import stdin
from collections import defaultdict


input = lambda: stdin.readline().rstrip()


if __name__ == "__main__":
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    cnts = defaultdict(int)
    left, ans = 0, 0
    for right in range(N):
        cnts[arr[right]] += 1
        while cnts[arr[right]] > K:
            cnts[arr[left]] -= 1
            left += 1
        ans = max(right - left + 1, ans)

    print(ans)
