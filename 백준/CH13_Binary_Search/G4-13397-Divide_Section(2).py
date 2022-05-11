"""
시간 초과
"""
from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 9)


def dfs(start, cnt, max_score):
    global ans

    score = max(arr[start:]) - min(arr[start:])
    ans = min(max(max_score, score), ans)

    if cnt < M:
        for end in range(start, N - 1):
            max_score = max(max(arr[start:end + 1]) - min(arr[start:end + 1]), max_score)
            dfs(end + 1, cnt + 1, max_score)


if __name__ == "__main__":
    input = lambda: stdin.readline().rstrip()

    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    ans = 10000
    dfs(0, 1, 0)
    print(ans)
