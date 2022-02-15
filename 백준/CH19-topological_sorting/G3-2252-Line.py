from sys import stdin
from collections import defaultdict, deque
from typing import List


def topology_sort(n: int, graph, indegrees) -> List[int]:
    dq = deque()

    for i in range(1, n + 1):
        if indegrees[i] == 0:
            dq.append(i)

    res = []
    while dq:
        res.append(dq.popleft())

        for neighbor in graph[res[-1]]:
            indegrees[neighbor] -= 1
            if indegrees[neighbor] == 0:
                dq.append(neighbor)

    return res


def main():
    n, m = map(int, stdin.readline().split())
    graph = defaultdict(list)
    indegrees = defaultdict(int)
    for _ in range(m):
        a, b = map(int, stdin.readline().split())
        graph[a].append(b)
        indegrees[b] += 1

    print(*topology_sort(n, graph, indegrees))


if __name__ == "__main__":
    main()
