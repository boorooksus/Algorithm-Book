from sys import stdin


def main():
    def input():
        return stdin.readline().rstrip()

    N, M, L = map(int, input().split())
    stations = [0] + list(map(int, input().split())) + [L]

    stations.sort()
    dists = list(stations[i + 1] - stations[i] for i in range(len(stations) - 1))

    res = 0
    start, end = 1, L
    while start <= end:
        mid = start + (end - start) // 2
        cnt = 0
        for dist in dists:
            if dist > mid:
                cnt += (dist - 1) // mid

        if cnt <= M:
            res = mid
            end = mid - 1
        else:
            start = mid + 1

    print(res)


if __name__ == "__main__":
    main()
