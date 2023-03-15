from sys import stdin
input = lambda: stdin.readline().rstrip()


INF = int(1e6)


def floyd_warshall() -> None:
    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(i + 1, N + 1):
                if dists[i][j] > dists[i][k] + dists[k][j]:
                    dists[i][j] = dists[i][k] + dists[k][j]
                    dists[j][i] = dists[j][k] + dists[k][i]


def get_time(a: int, b: int) -> int:
    res = 0
    for i in range(1, N + 1):
        if i != a and i != b:
            res += min(dists[a][i], dists[b][i]) * 2
    return res


if __name__ == "__main__":
    N, M = map(int, input().split())
    dists = [[INF] * (N + 1) for _ in range(N + 1)]

    for _ in range(M):
        a, b = map(int, input().split())
        dists[a][b], dists[b][a] = 1, 1

    floyd_warshall()

    ans = [0, 0, 1_000_000]
    for i in range(1, N):
        for j in range(i + 1, N + 1):
            temp = get_time(i, j)
            if temp < ans[2]:
                ans = [i, j, temp]

    print(*ans)

"""
Floyd Warshall + Brute Force 이용한 방법
속도가 더 빠름
"""