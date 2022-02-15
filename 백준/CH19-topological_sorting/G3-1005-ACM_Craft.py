from sys import stdin
from collections import defaultdict, deque


def topology_sort(n, w, costs, graph, indegrees) -> int:
    dp = [0] * (n + 1)
    dq = deque()

    for node in range(1, n + 1):
        if indegrees[node] == 0:
            dq.append(node)
            dp[node] = costs[node]

    while dq:
        node = dq.popleft()
        for neighbor in graph[node]:
            dp[neighbor] = max(dp[node] + costs[neighbor], dp[neighbor])
            indegrees[neighbor] -= 1
            if indegrees[neighbor] == 0:
                dq.append(neighbor)

    return dp[w]


def main():
    def input():
        return stdin.readline().rstrip()

    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        costs = [0] + list(map(int, input().split()))
        graph = defaultdict(list)
        indegrees = defaultdict(int)
        for _ in range(k):
            x, y = map(int, input().split())
            graph[x].append(y)
            indegrees[y] += 1
        w = int(input())
        print(topology_sort(n, w, costs, graph, indegrees))


if __name__ == "__main__":
    main()
