import sys
from collections import defaultdict, deque


def input():
    return sys.stdin.readline().strip()


n = m = 0
graph = defaultdict(list)
indeg = defaultdict(int)


def topology() -> None:
    global n, m
    dq = deque()
    res = [0] * (n + 1)

    for i in range(1, n + 1):
        if indeg[i] == 0:
            dq.append((i, 1))

    while dq:
        node, semester = dq.popleft()
        res[node] = semester

        for neighbor in graph[node]:
            indeg[neighbor] -= 1

            if indeg[neighbor] == 0:
                dq.append((neighbor, semester + 1))

    print(*res[1:])


def main():
    global n, m
    n, m = map(int, input().split())
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        indeg[b] += 1

    topology()


if __name__ == "__main__":
    main()
