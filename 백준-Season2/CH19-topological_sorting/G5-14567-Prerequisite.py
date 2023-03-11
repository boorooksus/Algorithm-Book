from sys import stdin
from collections import defaultdict, deque
input = lambda: stdin.readline().rstrip()


def topology_sort() -> None:
    dq = deque()
    for i in range(1, N + 1):
        if indegrees[i] == 0:
            dq.append((i, 1))  # (subject, semester)

    ans = [0] * (N + 1)
    while dq:
        subj, sem = dq.popleft()
        ans[subj] = sem
        for node in graph[subj]:
            indegrees[node] -= 1
            if indegrees[node] == 0:
                dq.append((node, sem + 1))

    print(*ans[1:], sep=' ')


if __name__ == "__main__":
    N, M = map(int, input().split())
    indegrees = [0] * (N + 1)
    graph = defaultdict(list)

    for _ in range(M):
        a, b = map(int, input().split())
        indegrees[b] += 1
        graph[a].append(b)

    topology_sort()
