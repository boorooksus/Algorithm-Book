"""
다익스트라 알고리즘
"""
from sys import stdin
from heapq import heappop, heappush


INF = 10001
dists, res = [], []


# 다익스트라 알고리즘
def dijkstra(start: int, n: int) -> None:
    global dists, res

    hq = []
    for i in range(1, n + 1):
        if i == start:
            continue
        heappush(hq, (dists[start][i], i))

    while hq:
        dist, node = heappop(hq)

        if dists[start][node] < dist:
            continue
        for neighbor in range(1, n + 1):
            # 자기 자신으로 가는 경로는 제외
            if node == neighbor or start == neighbor:
                continue
            # node를 우회할 때 start에서 neighbor 까지의 최단거리가 되는 경우
            if dist + dists[node][neighbor] < dists[start][neighbor]:
                dists[start][neighbor] = dist + dists[node][neighbor]
                heappush(hq, (dist + dists[node][neighbor], neighbor))
                # node로 가는 첫 번째 집하장을 neighbor 경로에 저장
                res[start][neighbor] = res[start][node]


def main():
    def input():
        return stdin.readline().rstrip()

    global dists, res

    n, m = map(int, input().split())
    dists = list(([INF] * (n + 1)) for _ in range(n + 1))
    res = [['-'] * (n + 1) for _ in range(n + 1)]

    for _ in range(m):
        a, b, w = map(int, input().split())
        dists[a][b] = dists[b][a] = w
        res[a][b] = str(b)
        res[b][a] = str(a)

    # 각 지점별로 다익스트라 알고리즘 수행
    for i in range(1, n + 1):
        dijkstra(i, n)

    for line in res[1:]:
        print(*line[1:], sep=' ')


if __name__ == "__main__":
    main()
