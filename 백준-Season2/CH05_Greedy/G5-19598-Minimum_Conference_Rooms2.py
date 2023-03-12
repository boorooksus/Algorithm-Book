from sys import stdin
input = lambda: stdin.readline().rstrip()


if __name__ == "__main__":
    N = int(input())
    times = []
    for _ in range(N):
        start, end = map(int, input().split())
        times += [(start, 1), (end, -1)]

    times.sort()
    res, cnt = 0, 0
    for _, flag in times:
        cnt += flag
        res = max(res, cnt)
    print(res)
