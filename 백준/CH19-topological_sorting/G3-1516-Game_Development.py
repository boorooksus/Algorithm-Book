"""
topology sorting + heapq
"""
from sys import stdin
from collections import defaultdict
from typing import List
from heapq import heappush, heappop


input = lambda: stdin.readline().rstrip()


def topology_sorting() -> List[int]:
    hq = []
    for i in range(1, N + 1):
        if indegrees[i] == 0:
            heappush(hq, (times[i], i))

    res = [0] * (N + 1)
    for _ in range(N):
        if not hq:
            break
        time, node = heappop(hq)
        res[node] = time
        for next in graph[node]:
            indegrees[next] -= 1
            if indegrees[next] == 0:
                heappush(hq, (time + times[next], next))

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
