from sys import stdin
input = lambda: stdin.readline().rstrip()


directions = [('N', 'E'), ('E', 'S'), ('S', 'W'), ('W', 'N')]
crds = {'N': (-1, 0), 'S': (1, 0), 'E': (0, 1), 'W': (0, -1)}


def dfs(cy: int, cx: int) -> int:
    res = 0
    while cy < N:
        while cx < M:
            if not visit[cy][cx]:
                strength = wood[cy][cx] * 2
                visit[cy][cx] = True
                for d in directions:
                    ny1, nx1 = cy + crds[d[0]][0], cx + crds[d[0]][1]
                    ny2, nx2 = cy + crds[d[1]][0], cx + crds[d[1]][1]
                    if 0 <= ny1 < N and 0 <= nx1 < M and 0 <= ny2 < N and 0 <= nx2 < M \
                            and not visit[ny1][nx1] and not visit[ny2][nx2]:
                        visit[ny1][nx1], visit[ny2][nx2] = True, True
                        res = max(res, wood[ny1][nx1] + wood[ny2][nx2] + strength + dfs(cy, cx + 1))
                        visit[ny1][nx1], visit[ny2][nx2] = False, False
                visit[cy][cx] = False
            cx += 1

        cx = 0
        cy += 1

    return res


if __name__ == "__main__":
    N, M = map(int, input().split())
    wood = list(list(map(int, input().split())) for _ in range(N))

    visit = list([False] * M for _ in range(N))
    print(dfs(0, 0))
