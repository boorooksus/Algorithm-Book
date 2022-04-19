from sys import stdin
from collections import deque, defaultdict


def topology_sorting() -> int:
    graph = defaultdict(list)
    for i in range(1, N + 1):
        for j in range(2, 2 + tasks[i][1]):
            graph[tasks[i][j]].append(i)

    dp = [0] * (N + 1)
    dq = deque()
    for i in range(1, N + 1):
        if tasks[i][1] == 0:
            dq.append(i)
            dp[i] = tasks[i][0]

    while dq:
        task = dq.popleft()

        for neighbor in graph[task]:
            tasks[neighbor][1] -= 1
            dp[neighbor] = max(dp[task] + tasks[neighbor][0], dp[neighbor])

            if tasks[neighbor][1] == 0:
                dq.append(neighbor)

    return max(dp)


if __name__ == "__main__":
    def input():
        return stdin.readline().rstrip()

    N = int(input())
    tasks = [[]] + \
            [list(map(int, input().split())) for _ in range(N)]

    print(topology_sorting())
