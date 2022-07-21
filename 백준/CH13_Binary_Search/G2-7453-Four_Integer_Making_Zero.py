"""
시간 초과
"""
from sys import stdin
from bisect import bisect_left
input = lambda: stdin.readline().rstrip()


if __name__ == "__main__":
    n = int(input())
    arr = [[0] * n for _ in range(4)]
    for i in range(n):
        temp = list(map(int, input().split()))
        for j in range(4):
            arr[j][i] = temp[j]

    for i in range(4):
        arr[i].sort()

    ans = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                l = bisect_left(arr[3], -(arr[0][i] + arr[1][j] + arr[2][k]))
                while n > l >= 0 == arr[0][i] + arr[1][j] + arr[2][k] + arr[3][l]:
                    ans += 1
                    l += 1

    print(ans)
