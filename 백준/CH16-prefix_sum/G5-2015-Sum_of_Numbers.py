from sys import stdin
from collections import defaultdict


def main():
    n, k = map(int, stdin.readline().split())
    arr = [0] + list(map(int, stdin.readline().split()))

    for i in range(1, n + 1):
        arr[i] += arr[i - 1]

    cnts = defaultdict(int)
    ans = 0
    for i in range(1, n + 1):
        if arr[i] == k:
            ans += 1
        ans += cnts[arr[i] - k]
        cnts[arr[i]] += 1

    print(ans)


if __name__ == "__main__":
    main()
