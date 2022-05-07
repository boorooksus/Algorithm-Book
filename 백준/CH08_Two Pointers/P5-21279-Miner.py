"""
풀이 참고: https://dev-splin.github.io/coding%20test/baekjoon/BaekJoon-Java-BruteForce-21279/

"""
from sys import stdin
from collections import defaultdict


MAXN = 100_000


if __name__ == "__main__":
    input = lambda: stdin.readline().rstrip()

    N, C = map(int, input().split())

    minerals = defaultdict(list)
    for _ in range(N):
        x, y, v = map(int, input().split())
        minerals[y].append([x, v])

    beauty, ans, cnt, y = 0, 0, 0, 0
    col_v = defaultdict(int)
    col_c = defaultdict(int)
    for x in range(MAXN, -1, -1):
        while cnt < C and y <= MAXN:
            for mineral in minerals[y]:
                if mineral[0] <= x:
                    beauty += mineral[1]
                    cnt += 1
                    col_v[mineral[0]] += mineral[1]
                    col_c[mineral[0]] += 1
            y += 1

        if cnt <= C and ans < beauty:
            ans = beauty

        if col_c[x] != 0:
            beauty -= col_v[x]
            cnt -= col_c[x]

    print(ans)
