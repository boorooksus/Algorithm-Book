from sys import stdin
from collections import defaultdict, deque


start, dest = 0, 0
graph = defaultdict(list)


def bfs(weight: int) -> bool:
    visit = defaultdict(bool)
    visit[start] = True
    dq = deque([start])

    while dq:
        node = dq.popleft()
        for neighbor, limit in graph[node]:
            if not visit[neighbor] and weight <= limit:
                if neighbor == dest:
                    return True
                visit[neighbor] = True
                dq.append(neighbor)
    return False


def main():
    def input():
        return stdin.readline().rstrip()
    global start, dest

    n, m = map(int, input().split())
    low, high = 0, 0
    for _ in range(m):
        a, b, w = map(int, input().split())
        graph[a].append((b, w))
        graph[b].append((a, w))
        high = max(w, high)
    start, dest = map(int, stdin.readline().split())

    res = 0
    while low <= high:
        mid = low + (high - low) // 2
        if bfs(mid):
            res = mid
            low = mid + 1
        else:
            high = mid - 1

    print(res)


if __name__ == "__main__":
    main()
