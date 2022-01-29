import sys
from collections import defaultdict, deque
from typing import List


class Solution:
    def __init__(self, n, m, k, x, roads):
        self.n, self.m, self.k, self.x = n, m, k, x
        self.graph = defaultdict(list)
        for a, b in roads:
            self.graph[a].append(b)

    def bfs(self) -> List[int]:
        visit = [False] * (self.n + 1)
        dq = deque([self.x])
        visit[self.x] = True
        dist = -1
        while dq:
            dist += 1

            if dist == self.k:
                return sorted(list(dq))

            s = len(dq)
            for i in range(s):
                city = dq.popleft()

                for neighbor in self.graph[city]:
                    if not visit[neighbor]:
                        visit[neighbor] = True
                        dq.append(neighbor)

        return [-1]


def main():
    def input():
        return sys.stdin.readline().strip()

    n, m, k, x = map(int, input().split())
    roads = []
    for _ in range(m):
        roads.append(tuple(map(int, input().split())))

    res = Solution(n, m, k, x, roads).bfs()
    for city in res:
        print(city)


if __name__ == "__main__":
    main()
