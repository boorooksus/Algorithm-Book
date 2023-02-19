from sys import stdin
input = lambda: stdin.readline().rstrip()


def binary_search() -> int:
    left, right = 1, max(times) * M
    res = 0
    while left <= right:
        mid = left + (right - left) // 2
        passed = 0

        for time in times:
            passed += mid // time

        if passed < M:
            left = mid + 1
        else:
            res = mid
            right = mid - 1

    return res


if __name__ == "__main__":
    N, M = map(int, input().split())
    times = list(int(input()) for _ in range(N))

    print(binary_search())
