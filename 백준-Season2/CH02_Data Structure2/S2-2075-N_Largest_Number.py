from sys import stdin
from heapq import heappush, heappop
input = lambda: stdin.readline().rstrip()


if __name__ == "__main__":
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    hq = []
    for i in range(N):
        heappush(hq, (-arr[i][-1], i, N - 1))

    for _ in range(N - 1):
        _, i, j = heappop(hq)
        heappush(hq, (-arr[i][j - 1], i, j - 1))

    print(-hq[0][0])


"""
메모리 초과
"""