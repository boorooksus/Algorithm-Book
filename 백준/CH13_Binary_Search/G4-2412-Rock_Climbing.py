"""
bfs 이용한 풀이
시간 초과
"""
from sys import stdin
from collections import deque


input = lambda: stdin.readline().rstrip()
INF = 50002


def bfs(cnt: int) -> int:
    visit = [False] * (n + 1)
    dq = deque([(0, 0)])
    while dq:
        move, idx = dq.popleft()
        if move > cnt:
            return -1
        elif holds[idx][1] == T:
            return move
        for i in range(1, n + 1):
            if abs(holds[i][1] - holds[idx][1]) <= 2 and abs(holds[i][0] - holds[idx][0]) <= 2:
                visit[i] = True
                dq.append((move + 1, i))
    return -1


if __name__ == "__main__":
    n, T = map(int, input().split())
    holds = [[0, 0]] + sorted(list(list(map(int, input().split())) for _ in range(n)), key=lambda crd: crd[1])
    print(bfs(n + 1))

