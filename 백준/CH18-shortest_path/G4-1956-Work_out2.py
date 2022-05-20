from sys import stdin


input = lambda: stdin.readline().rstrip()
INF = 4_000_000_000


def floyd_warshall() -> int:
    for k in range(1, V + 1):
        for i in range(1, V + 1):
            for j in range(1, V + 1):
                if graph[i][k] == INF:
                    break
                graph[i][j] = min(graph[i][k] + graph[k][j],
                                  graph[i][j])

    res = INF
    for i in range(1, V + 1):
        res = min(graph[i][i], res)
    return res


if __name__ == "__main__":
    V, E = map(int, input().split())
    graph = list([INF] * (V + 1) for _ in range(V + 1))
    for _ in range(E):
        a, b, c = map(int, input().split())
        graph[a][b] = c

    ans = floyd_warshall()
    print([-1, ans][ans != INF])

