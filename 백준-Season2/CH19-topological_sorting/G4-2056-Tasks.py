from sys import stdin
from collections import deque, defaultdict
input = lambda: stdin.readline().rstrip()


def topology_sorting() -> int:
    costs = [0] * (N + 1)
    dq = deque()
    for i in range(1, N + 1):
        if indgrs[i] == 0:
            costs[i] = times[i]
            dq.append((i, times[i]))

    while dq:
        node, cur = dq.popleft()
        for nxt in graph[node]:
            indgrs[nxt] -= 1
            costs[nxt] = max(costs[nxt], cur + times[nxt])
            if indgrs[nxt] == 0:
                dq.append((nxt, costs[nxt]))

    return max(costs)


if __name__ == "__main__":
    N = int(input())

    graph = defaultdict(list)
    indgrs = defaultdict(int)
    times = defaultdict(int)
    for i in range(1, N + 1):
        li = list(map(int, input().split()))
        times[i] = li[0]
        indgrs[i] = li[1]
        for j in range(2, len(li)):
            graph[li[j]].append(i)

    print(topology_sorting())
