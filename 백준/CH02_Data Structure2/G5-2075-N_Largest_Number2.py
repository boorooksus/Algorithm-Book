from sys import stdin
from bisect import bisect_right
from collections import deque


def main():
    def input():
        return stdin.readline().rstrip()

    n = int(input())
    window = deque(list(map(int, input().split())))
    for i in range(1, n):
        row = list(map(int, input().split()))
        for num in row:
            idx = bisect_right(window, num)
            if idx > 0:
                window.insert(idx, num)
                window.popleft()

    print(window[0])


if __name__ == "__main__":
    main()
