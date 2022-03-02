"""
플로이드 와샬 알고리즘
"""
from sys import stdin
from typing import List


INF = 10001


# 플로이드 와샬 알고리즘
def floyd_warshall(n: int, dists: List[List[int]], res: List[List[str]]) -> List[List[str]]:
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                # 자기 자신으로 가는 경로는 제외
                if i == j:
                    continue
                # k를 우회할 때 최단거리가 되는 경우
                if dists[i][j] > dists[i][k] + dists[k][j]:
                    dists[i][j] = dists[i][k] + dists[k][j]
                    # k로 가기 위한 첫 번째 집하장을 저장
                    res[i][j] = res[i][k]
    return res


def main():
    def input():
        return stdin.readline().rstrip()

    n, m = map(int, input().split())
    dists = list(([INF] * (n + 1)) for _ in range(n + 1))
    res = [['-'] * (n + 1) for _ in range(n + 1)]

    for _ in range(m):
        a, b, w = map(int, input().split())
        dists[a][b] = dists[b][a] = w
        res[a][b] = str(b)
        res[b][a] = str(a)

    res = floyd_warshall(n, dists, res)

    for line in res[1:]:
        print(*line[1:], sep=' ')


if __name__ == "__main__":
    main()
