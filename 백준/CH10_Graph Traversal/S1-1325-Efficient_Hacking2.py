from sys import stdin
from collections import defaultdict, deque


def bfs(start: int, n: int, graph: defaultdict[int]) -> int:
    visit = [False] * (n + 1)
    cnt = 0
    dq = deque([start])
    visit[start] = True
    while dq:
        node = dq.pop()
        for neighbor in graph[node]:
            if not visit[neighbor]:
                visit[neighbor] = True
                dq.append(neighbor)
                cnt += 1
    return cnt


def main():
    def input():
        return stdin.readline().rstrip()

    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        a, b = map(int, input().split())
        graph[b].append(a)

    res = []
    max_cnt = 0
    for i in range(1, n + 1):
        cnt = bfs(i, n, graph)
        if cnt > max_cnt:
            max_cnt = cnt
            res = [i]
        elif cnt == max_cnt:
            res.append(i)

    print(*sorted(res), sep=' ')


if __name__ == "__main__":
    main()
