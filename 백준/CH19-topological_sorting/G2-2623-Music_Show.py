from sys import stdin
from collections import defaultdict, deque
from typing import List


graph = defaultdict(list)
indegrees = defaultdict(int)


def topology(n: int) -> List[int]:
    dq = deque()
    for i in range(1, n + 1):
        if indegrees[i] == 0:
            dq.append(i)

    res = []
    while dq:
        for _ in range(n):
            if not dq:
                return [0]
            node = dq.popleft()
            res.append(node)
            for neighbor in graph[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    dq.append(neighbor)
    return res


def main():
    def input():
        return stdin.readline().rstrip()

    n, m = map(int, input().split())
    for _ in range(m):
        order = list(map(int, input().split()))
        for i in range(1, len(order) - 1):
            graph[order[i]].append(order[i + 1])
            indegrees[order[i + 1]] += 1

    print(*topology(n), sep="\n")


if __name__ == "__main__":
    main()
