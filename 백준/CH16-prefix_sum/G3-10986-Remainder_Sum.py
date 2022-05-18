"""
시간초과
"""
from sys import stdin


input = lambda: stdin.readline().rstrip()


if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = [0] + list(map(int, input().split()))

    ans = 0
    for i in range(1, N + 1):
        arr[i] += arr[i - 1]

        for j in range(i):
            tmp = arr[i] - arr[j]
            if (arr[i] - arr[j]) % M == 0:
                ans += 1

    print(ans)
