"""
Network Flow 이용
"""
from sys import stdin, maxsize
from collections import defaultdict, deque


input = lambda: stdin.readline().rstrip()


def max_flow() -> int:
    res = 0
    while True:
        dq = deque([start])
        visit = [-1] * (end + 1)
        while dq:
            node = dq.popleft()
            for neighbor in graph[node]:
                if c[node][neighbor] - f[node][neighbor] > 0 and visit[neighbor] == -1:
                    visit[neighbor] = node
                    dq.append(neighbor)
                    if neighbor == end:
                        break
        if visit[end] == -1:
            break

        flow = maxsize
        i = end
        while i != start:
            flow = min(flow, c[visit[i]][i] - f[visit[i]][i])
            i = visit[i]

        i = end
        while i != start:
            f[visit[i]][i] += flow
            f[i][visit[i]] -= flow
            i = visit[i]

        res += flow

    return res


if __name__ == "__main__":
    N, M, K = map(int, input().split())
    start, mid, end = 0, N + M + 1, N + M + 2  # 시작 노드, 벌점 노드, 종점 노드
    c = list([0] * (end + 1) for _ in range(end + 1))  # capacities
    f = list([0] * (end + 1) for _ in range(end + 1))  # flows
    graph = defaultdict(list)

    # 시작 노드와 벌점 노드 연결 (유량 K)
    graph[start].append(mid)
    graph[mid].append(start)
    c[start][mid] = K

    # 시작 - 직원 노드 (유량 1) , 시작 - 벌점 노드 (유량 K) 연결
    for i in range(1, N + 1):
        graph[start].append(i)
        graph[i].append(start)
        graph[mid].append(i)
        graph[i].append(mid)
        c[start][i] = 1
        c[mid][i] = K

    # 직원 - 업무 노드 연결 (유량 1)
    for i in range(1, N + 1):
        temp = list(map(int, input().split()))
        for j in range(1, len(temp)):
            graph[i].append(N + temp[j])
            graph[N + temp[j]].append(i)
            c[i][N + temp[j]] = 1

    # 업무 -종점 노드 연결 (유량 1)
    for i in range(1, M + 1):
        graph[N + i].append(end)
        graph[end].append(N + i)
        c[N + i][end] = 1

    print(max_flow())
