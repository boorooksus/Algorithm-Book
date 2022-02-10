from sys import stdin
from bisect import bisect_left, bisect_right


n, m = map(int, stdin.readline().split())
points = list(map(int, stdin.readline().split()))
lines = list(tuple(map(int, stdin.readline().split())) for _ in range(m))

points.sort()
for line in lines:
    start = bisect_left(points, line[0])
    end = bisect_right(points, line[1])

    print(end - start)
