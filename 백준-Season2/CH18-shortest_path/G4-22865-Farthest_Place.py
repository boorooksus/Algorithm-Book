from sys import stdin
input = lambda: stdin.readline().rstrip()


INF = int(1e9)


def floyd_warshall() -> int:
    for i in range(1, N + 1):
        graph[i][i] = 0

    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(i + 1, N + 1):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
                    graph[j][i] = graph[i][k] + graph[k][j]

    land, dist = 0, -1

    for i in range(1, N + 1):
        min_friend, min_dist = 0, INF
        for friend in friends:
            if min_dist > graph[friend][i]:
                min_friend, min_dist = friend, graph[friend][i]
        if dist < min_dist:
            land, dist = i, min_dist

    return land


if __name__ == "__main__":
    N = int(input())
    friends = list(map(int, input().split()))
    M = int(input())

    graph = [[INF] * (N + 1) for _ in range(N + 1)]
    for _ in range(M):
        a, b, d = map(int, input().split())
        graph[a][b] = d
        graph[b][a] = d

    print(floyd_warshall())


"""
시간 초과
"""