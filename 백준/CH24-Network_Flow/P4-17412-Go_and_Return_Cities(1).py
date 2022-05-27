from sys import stdin, maxsize
from collections import defaultdict, deque


input = lambda: stdin.readline().rstrip()


def max_flow(start: int, end: int) -> int:
    res = 0
    while True:
        prevs = [-1] * (N + 1)
        dq = deque([start])
        while dq:
            node = dq.popleft()
            for neighbor in graph[node]:
                if capacities[node][neighbor] - flows[node][neighbor] > 0 and prevs[neighbor] == -1:
                    dq.append(neighbor)
                    prevs[neighbor] = node
                    if neighbor == end:
                        break
        if prevs[end] == -1:
            break

        flow = maxsize
        i = end
        while i != start:
            flow = min(flow, capacities[prevs[i]][i] - flows[prevs[i]][i])
            i = prevs[i]

        i = end
        while i != start:
            flows[prevs[i]][i] += flow
            flows[i][prevs[i]] -= flow
            i = prevs[i]

        res += flow

    return res


if __name__ == "__main__":
    N, P = map(int, input().split())
    graph = defaultdict(list)
    capacities = list([0] * (N + 1) for _ in range(N + 1))
    # capacities = list([1] * (N + 1) for _ in range(N + 1))
    flows = list([0] * (N + 1) for _ in range(N + 1))
    for _ in range(P):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        capacities[a][b] = 1
    print(max_flow(1, 2))
