"""
시간초과
"""
from sys import stdin
from itertools import combinations


input = lambda: stdin.readline().rstrip()


if __name__ == "__main__":
    N, K = map(int, input().split())
    num = int(input())

    ans = 0
    for comb in combinations(list(i for i in str(num)), N - K):
        res = int(''.join(comb))
        ans = max(res, ans)
    print(ans)