from sys import stdin


INF = 10001


def floyd_warshall() -> None:
    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):
                if graph[i][k] + graph[k][j] < graph[i][j]:
                    graph[i][j] = 0

    res = set()
    for i in range(len(graph)):
        for j in range(len(graph)):
            if i != j and graph[i][j] == 0:
                res.add(chr(i + 65) + " => " + chr(j + 65))

    print(len(res))
    print(*sorted(res), sep="\n")


if __name__ == "__main__":
    def input():
        return stdin.readline().rstrip()

    N = int(input())
    graph = list([INF] * 58 for _ in range(58))
    for _ in range(N):
        x = list(input().split())
        if x[0] != x[-1]:
            graph[ord(x[0]) - 65][ord(x[-1]) - 65] = 0

    floyd_warshall()
