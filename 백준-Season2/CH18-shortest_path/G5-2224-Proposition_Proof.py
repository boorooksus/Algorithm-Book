from sys import stdin
input = lambda: stdin.readline().rstrip()


INF = 10001


def floyd_warshall() -> None:
    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):
                if i != j and graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = 0

    ans = set()
    for i in range(len(graph)):
        for j in range(len(graph)):
            if i != j and graph[i][j] == 0:
                ans.add(chr(i + 65) + " => " + chr(j + 65))

    print(len(ans))
    print(*sorted(ans), sep="\n")


if __name__ == "__main__":
    N = int(input())

    graph = list([INF] * 58 for _ in range(58))
    for _ in range(N):
        p, q = input().split(" => ")
        graph[ord(p) - 65][ord(q) - 65] = 0

    floyd_warshall()
