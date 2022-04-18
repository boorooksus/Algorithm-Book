"""
Topology Sort
틀림
사이클이 존재하는 경우, 
indegree가 0인 노드가 없어서 명제 생성 불가
"""
from sys import stdin
from collections import defaultdict, deque
from typing import List


def topology_sort() -> List[str]:
    lefts = deque()
    for i in graph.keys():
        if indegrees[i] == 0:
            lefts.append((i, []))

    res = set()
    while lefts:
        left, route = lefts.popleft()
        for right in graph[left]:
            res.add(left + " => " + right)
            for prev in route:
                if prev != right:
                    res.add(prev + " => " + right)

            indegrees[right] -= 1
            if indegrees[right] == 0:
                lefts.append((right, route + [left]))

    return sorted(list(res))


if __name__ == "__main__":
    def input():
        return stdin.readline().rstrip()

    N = int(input())
    graph = defaultdict(list)
    indegrees = defaultdict(int)
    for _ in range(N):
        x = list(input().split())
        if x[0] != x[-1]:
            graph[x[0]].append(x[-1])
            indegrees[x[-1]] += 1

    res = topology_sort()
    print(len(res))
    print(*res, sep="\n")