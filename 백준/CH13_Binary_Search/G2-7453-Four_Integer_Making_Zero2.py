"""
시간 초과
"""
from sys import stdin
from collections import defaultdict
input = lambda: stdin.readline().rstrip()


if __name__ == "__main__":
    n = int(input())
    arr = list(list(map(int, input().split())) for _ in range(n))

    ab = defaultdict(int)
    for i in range(n):
        for j in range(n):
            ab[arr[i][0] + arr[j][1]] += 1

    ans = 0
    for i in range(n):
        for j in range(n):
            temp = arr[i][2] + arr[j][3]
            ans += ab[-temp]
    print(ans)

