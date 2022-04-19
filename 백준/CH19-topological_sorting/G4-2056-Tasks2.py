from sys import stdin
from collections import defaultdict


if __name__ == "__main__":
    def input():
        return stdin.readline().rstrip()

    N = int(input())
    times = [0] * (N + 1)
    prevs = defaultdict(list)
    for i in range(1, N + 1):
        x = list(map(int, input().split()))
        times[i] = x[0]
        for j in range(2, 2 + x[1]):
            prevs[i].append(x[j])

    for i in range(1, N + 1):
        time = 0
        for j in prevs[i]:
            time = max(times[j], time)
        times[i] += time

    print(max(times))
