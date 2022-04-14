from sys import stdin, maxsize


def dfs(cy, cx, hp, durab, total):
    global ans

    move = abs(cy - ey) + abs(cx - ex)
    if move <= hp + durab:
        ans = min(total + move, ans)
        return

    for uy, ux in umbs:
        if not visit[uy][ux]:
            nh, nd = hp, durab
            move = abs(cy - uy) + abs(cx - ux)
            if move > nd:
                nh -= move - nd
            if nh >= 0:
                visit[uy][ux] = True
                dfs(uy, ux, nh, D, total + move)
                visit[uy][ux] = False


if __name__ == "__main__":
    def input():
        return stdin.readline().rstrip()


    N, H, D = map(int, input().split())
    arr = [input() for _ in range(N)]

    visit = list([False] * N for _ in range(N))
    # (sy, sx): 시작 위치, (ey, ex): 도착 위치
    sy, sx, ey, ex = 0, 0, 0, 0
    umbs = []
    ans = maxsize
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'S':
                sy, sx = i, j
            elif arr[i][j] == 'E':
                ey, ex = i, j
            elif arr[i][j] == 'U':
                umbs.append((i, j))

    dfs(sy, sx, H, 0, 0)
    print([-1, ans][ans != maxsize])
