from sys import stdin
input = lambda: stdin.readline().rstrip()
INF = 2_000_000_001


if __name__ == "__main__":
    N = int(input())
    sols = list(map(int, input().split()))

    sols.sort()
    left, right = 0, N - 1
    res = (sols[left], sols[right])
    min_val = INF
    while left < right:
        temp = sols[left] + sols[right]

        if abs(temp) < min_val:
            min_val = abs(temp)
            res = (sols[left], sols[right])

        if temp == 0:
            break
        elif temp < 0:
            left += 1
        else:
            right -= 1

    print(*res)
