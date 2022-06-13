from sys import stdin


if __name__ == "__main__":
    N, k = (int(stdin.readline()) for _ in range(2))
    start, end = 1, k
    ans = 0
    while start <= end:
        mid = start + (end - start) // 2
        temp = 0
        for i in range(1, N + 1):
            temp += min(mid // i, N)

        if temp >= k:
            ans = mid
            end = mid - 1
        else:
            start = mid + 1

    print(ans)