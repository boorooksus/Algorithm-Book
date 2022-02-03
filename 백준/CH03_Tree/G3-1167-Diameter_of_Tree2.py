from sys import stdin
from collections import defaultdict, deque


graph = defaultdict(list)
v = 0


def main():
    def input():
        return stdin.readline().rstrip()

    global graph, v

    v = int(input())

    for _ in range(v):
        line = list(map(int, input().split()))
        for i in range(1, len(line) - 1, 2):
            graph[line[0]].append((line[i], line[i + 1]))

    node, dist = bfs(1)
    res = bfs(node)
    print(res[1])


def bfs(start: int) -> tuple[int, int]:
    res = (0, 0)  # (max distance, farthest node)
    visit = [-1] * (v + 1)

    dq = deque([(start, 0)])
    visit[start] = 0

    while dq:
        node, dist = dq.popleft()
        for neighbor, w in graph[node]:
            if visit[neighbor] == -1:
                visit[neighbor] = dist + w

                if visit[neighbor] > res[1]:
                    res = (neighbor, visit[neighbor])

                dq.appendleft((neighbor, visit[neighbor]))

    return res


if __name__ == "__main__":
    main()


"""
bfs 두 번을 통한 트리의 지름 구하기.
첫 번째 bfs -> 임의의 한 노드로 부터 가장 먼 노드 구함
두 번째 bfs -> 이전에 구한 가장 먼 노드로부터 가장 먼 거리를 구함
"""