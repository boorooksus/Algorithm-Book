from sys import stdin


def floyd_warshall(items, graph, n, m):
    cnts = [0] * (n + 1)

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i == j:
                    graph[i][j] = 0

                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][j] <= m:
                cnts[i] += items[j]

    return max(cnts)


def main():
    def input():
        return stdin.readline().rstrip()

    n, m, r = map(int, input().split())
    items = [0] + list(map(int, input().split()))
    graph = [[1500] * (n + 1) for _ in range(n + 1)]
    for _ in range(r):
        a, b, l = map(int, input().split())
        graph[a][b] = l
        graph[b][a] = l

    print(floyd_warshall(items, graph, n, m))


if __name__ == "__main__":
    main()
