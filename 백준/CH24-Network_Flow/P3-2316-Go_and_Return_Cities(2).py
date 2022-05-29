from sys import stdin, maxsize
from collections import defaultdict, deque


input = lambda: stdin.readline().rstrip()
PIVOT = 400
MAX = 801


def max_flow(start: int, end: int) -> int:
    res = 0
    while True:
        dq = deque([start])
        prevs = [-1] * MAX
        while dq:
            node = dq.popleft()
            for i in graph[node]:
                if prevs[i] == -1 and c[node][i] - f[node][i] > 0:
                    prevs[i] = node
                    dq.append(i)
                    if i == end:
                        break

        if prevs[end] == -1:
            break

        flow = maxsize
        i = end
        while i != start:
            flow = min(flow, c[prevs[i]][i] - f[prevs[i]][i])
            i = prevs[i]

        i = end
        while i != start:
            f[prevs[i]][i] += flow
            f[i][prevs[i]] -= flow
            i = prevs[i]

        res += flow

    return res


if __name__ == "__main__":
    N, P = map(int, input().split())
    c = list([0] * MAX for _ in range(MAX))
    f = list([0] * MAX for _ in range(MAX))
    graph = defaultdict(list)

    for i in range(1, N + 1):
        graph[i].append(i + PIVOT)
        graph[i + PIVOT].append(i)
        c[i][i + PIVOT] = 1

    for _ in range(P):
        a, b = map(int, input().split())

        graph[a + PIVOT].append(b)
        graph[b].append(a + PIVOT)

        graph[b + PIVOT].append(a)
        graph[a].append(b + PIVOT)

        c[a + PIVOT][b] = 1
        c[b + PIVOT][a] = 1

    print(max_flow(1 + PIVOT, 2))


"""
Network Flow + 정점 분할
1 ~ N: in 노드, 
PIVOT + 1 ~ PIVOT + N: out 노드
"""