from sys import stdin
from collections import defaultdict, deque
input = lambda: stdin.readline().rstrip()


def get_time(a: int, b: int) -> int:
    visit = defaultdict(bool)
    dq = deque([(a, 0), (b, 0)])
    visit[a], visit[b] = True, True

    res = 0
    while dq:
        cur, cnt = dq.popleft()
        for nxt in graph[cur]:
            if not visit[nxt]:
                visit[nxt] = True
                res += (cnt + 1) * 2
                dq.append((nxt, cnt + 1))

    return res


if __name__ == "__main__":
    N, M = map(int, input().split())
    graph = defaultdict(list)

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    ans = [0, 0, 1_000_000]
    for i in range(1, N):
        for j in range(i + 1, N + 1):
            temp = get_time(i, j)
            if temp < ans[2]:
                ans = [i, j, temp]

    print(*ans)

"""
BFS + Brute Force 이용한 방법
"""