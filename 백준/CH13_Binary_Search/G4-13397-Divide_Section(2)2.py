from sys import stdin


def check(pivot) -> bool:
    low, high = arr[0], arr[0]
    cnt = 1

    for i in range(1, N):
        low, high = min(arr[i], low), max(arr[i], high)

        if high - low > pivot:
            cnt += 1
            low, high = arr[i], arr[i]

    return cnt <= M


if __name__ == "__main__":
    input = lambda: stdin.readline().rstrip()

    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    ans = 10000
    start, end = 0, max(arr)
    while start <= end:
        mid = start + (end - start) // 2

        if check(mid):
            ans = mid
            end = mid - 1
        else:
            start = mid + 1

    print(ans)

