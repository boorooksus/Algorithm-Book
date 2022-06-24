"""
Heapq 사용 X 방식 -> 속도 개선
"""
from sys import stdin
from collections import defaultdict, deque
from typing import List


input = lambda: stdin.readline().rstrip()


def topology_sorting() -> List[int]:
    res = [0] * (N + 1)
    dq = deque()
    for i in range(1, N + 1):
        if indegrees[i] == 0:
            res[i] = times[i]
            dq.append(i)

    while dq:
        node = dq.popleft()
        for next in graph[node]:
            indegrees[next] -= 1
            res[next] = max(res[node] + times[next], res[next])
            if indegrees[next] == 0:
                dq.append(next)

    return res


if __name__ == "__main__":
    N = int(input())
    graph = defaultdict(list)
    times = [0] * (N + 1)
    indegrees = [0] * (N + 1)
    for i in range(1, N + 1):
        query = list(map(int, input().split()))
        times[i] = query[0]
        for j in range(1, len(query) - 1):
            graph[query[j]].append(i)
            indegrees[i] += 1

    ans = topology_sorting()
    print(*ans[1:], sep='\n')
