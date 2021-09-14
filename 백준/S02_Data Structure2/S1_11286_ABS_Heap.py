from sys import stdin
import heapq


n = int(stdin.readline())
hq = []

for _ in range(n):
    x = int(stdin.readline())

    if x == 0:
        print(heapq.heappop(hq)[1]) if hq else print(0)

    else:
        heapq.heappush(hq, (abs(x), x))

