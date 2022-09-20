from sys import stdin
from bisect import bisect_left
input = lambda: stdin.readline().rstrip()
INF = 3_000_000_001


if __name__ == "__main__":
    N = int(input())
    sols = sorted(list(map(int, input().split())))

    res = (0, 0, 0)
    min_val = INF
    for i in range(N - 2):
        if i > 0 and sols[i - 1] == sols[i]:
            continue

        left, right = i + 1, N - 1
        while left < right:
            temp = sols[i] + sols[left] + sols[right]

            if abs(temp) < min_val:
                min_val = abs(temp)
                res = (sols[i], sols[left], sols[right])

            if temp < 0:
                left += 1
                while sols[left - 1] == sols[left]:
                    left += 1
            elif temp > 0:
                right -= 1
                while sols[right] == sols[right + 1]:
                    right -= 1
            else:
                print(*res)
                exit(0)

    print(*res)
