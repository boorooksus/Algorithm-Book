import sys


def input():
    return sys.stdin.readline().strip()


n = 0
graph = []


def floyd_warshall() -> None:
    global n, graph

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1


def main():
    global n, graph

    n = int(input())
    for i in range(n):
        graph.append(list(map(int, input().split())))

    floyd_warshall()

    for i in range(n):
        print(*graph[i])


if __name__ == "__main__":
    main()
