from sys import stdin
from collections import deque
input = lambda: stdin.readline().rstrip()


def bfs() -> int:
    dq = deque([(0, 0, 0, [0, 1][arr[0][0] == 2])])  # (y, x, time, weapon)
    visit = list(list([False, False] for _ in range(M)) for _ in range(N))
    visit[0][0][0] = True

    while dq:
        cy, cx, ct, cw = dq.popleft()
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ny, nx, nw = cy + dy, cx + dx, cw
            if 0 <= ny < N and 0 <= nx < M and \
                    not visit[ny][nx][nw] and ct + 1 <= T and \
                    (arr[ny][nx] != 1 or cw):
                if ny == N - 1 and nx == M - 1:
                    return ct + 1
                if arr[ny][nx] == 2:
                    nw = 1
                dq.append((ny, nx, ct + 1, nw))
                visit[ny][nx][nw] = True

    return 0


if __name__ == "__main__":
    N, M, T = map(int, input().split())
    arr = list(list(map(int, input().split())) for _ in range(N))

    res = bfs()
    print(res if res > 0 else 'Fail')


"""
BFS 탐색 문제
문제 조건이 'T시간 이내' 인지, 'T시간 이하' 인지 잘 보기
visit 배열은 3차원 배열로 만들어서, 무기를 얻은 경우와 아닌 경우 분리하여 관리하기
"""