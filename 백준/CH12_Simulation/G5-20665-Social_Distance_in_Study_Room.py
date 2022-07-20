"""
틀림
"""
from sys import stdin
input = lambda: stdin.readline().rstrip()


def get_spot(cur: int) -> int:
    if spots[1] <= cur:
        return 1

    dist = N
    while dist:
        i = 2
        while dist * i <= N:
            if spots[dist * i] <= cur:
                return dist * i
            i += 1
        if spots[dist] <= cur:
            return dist
        dist //= 2
    return 0


if __name__ == "__main__":
    N, T, P = map(int, input().split())
    time = list(list(map(int, input().split())) for _ in range(T))

    for i in range(T):
        for j in range(2):
            time[i][j] = time[i][j] // 100 * 60 + time[i][j] % 100

    time.sort(key=lambda x: (x[0], x[1]))
    spots = [60 * 9] * (N + 1)
    ans = 0
    for start, end in time:
        spot = get_spot(start)
        if spot == P and spots[P] < start:
            ans += start - spots[P]
        spots[spot] = end
        if spots[P] < start:
            ans += start - spots[P]
            spots[P] = start
    ans += 60 * 21 - max(spots[P], time[-1][0])

    print(ans)
