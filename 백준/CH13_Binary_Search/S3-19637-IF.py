from sys import stdin
from bisect import bisect_left


if __name__ == "__main__":
    def input():
        return stdin.readline().rstrip()

    n, m = map(int, input().split())
    titles, max_values = [], []
    for _ in range(n):
        t, v = input().split()
        titles.append(t)
        max_values.append(int(v))
    for _ in range(m):
        x = int(input())
        idx = bisect_left(max_values, x)
        if idx >= 0:
            print(titles[idx])
        else:
            print(titles[0])
