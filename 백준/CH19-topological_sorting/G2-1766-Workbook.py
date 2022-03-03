from sys import stdin
from collections import defaultdict
from typing import List
from heapq import heappop, heappush


def topology(n: int, indegrees: defaultdict, graph: defaultdict) -> List[int]:
    hq = []
    # indegree가 0인 노드를 찾아 heap에 삽입
    for i in range(1, n + 1):
        if indegrees[i] == 0:
            heappush(hq, i)

    res = []
    # 위상 정렬 실행
    for _ in range(n):
        node = heappop(hq)
        res.append(node)
        for neighbor in graph[node]:
            indegrees[neighbor] -= 1

            if indegrees[neighbor] == 0:
                heappush(hq, neighbor)

    return res


def main():
    def input():
        return stdin.readline().rstrip()

    n, m = map(int, input().split())
    indegrees = defaultdict(int)
    graph = defaultdict(list)

    for _ in range(m):
        a, b = map(int, input().split())
        indegrees[b] += 1
        graph[a].append(b)

    print(*topology(n, indegrees, graph))


if __name__ == "__main__":
    main()
