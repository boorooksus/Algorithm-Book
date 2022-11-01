from collections import deque
from typing import List


def move_shark(y: int, x: int, cnt: int, route: List) -> None:
    global max_cnt, max_route

    move = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    cnt += len(graph[y][x])

    if len(route) > 3:
        if cnt > max_cnt:
            max_cnt, max_route = cnt, route
        return

    for d in range(len(move)):
        ny, nx = y + move[d][0], x + move[d][1]
        if 0 <= ny < 4 and 0 <= nx < 4 and (ny, nx) not in route:
            move_shark(ny, nx, cnt, route + [(ny, nx)])


def move_fish() -> None:
    move = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

    for y in range(4):
        for x in range(4):
            for fish in temp[y][x]:
                for d in range(fish, fish - 8, -1):
                    d %= len(move)
                    ny, nx = y + move[d][0], x + move[d][1]
                    if 0 <= ny < 4 and 0 <= nx < 4 and \
                            (ny, nx) != shark and not smell[ny][nx]:
                        graph[ny][nx].append(d)
                        break


if __name__ == "__main__":
    M, S = map(int, input().split())
    graph = list(list([] for _ in range(4)) for _ in range(4))
    for _ in range(M):
        x, y, d = map(int, input().split())
        graph[x - 1][y - 1].append(d - 1)
    shark = tuple(map(lambda x: int(x) - 1, input().split()))
    smell = list([0] * 4 for _ in range(4))

    for _ in range(S):
        # 1. 복제 마법 시전
        temp = graph[:]
        graph = list(list([] for _ in range(4)) for _ in range(4))

        # 2. 물고기 한 칸씩 이동
        move_fish()

        # 3-1. 상어 3칸 이동
        max_cnt, max_route = -1, []
        move_shark(shark[0], shark[1], 0, [shark])

        # 4. 두 번 전 물고기 냄새 제거
        for x in range(4):
            for y in range(4):
                if smell[y][x] > 0:
                    smell[y][x] -= 1

        # 3-2. 상어가 이동한 경로의 물고기 제거
        for y, x in max_route:
            if graph[y][x]:
                graph[y][x] = []
                smell[y][x] = 2
        shark = max_route[-1]

        # 5. 복제 마법 완료
        for y in range(4):
            for x in range(4):
                graph[y][x] += temp[y][x]

    cnt = 0
    for y in range(4):
        for x in range(4):
            cnt += len(graph[y][x])

    print(cnt)
