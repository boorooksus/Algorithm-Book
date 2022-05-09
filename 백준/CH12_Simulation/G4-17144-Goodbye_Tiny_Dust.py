from sys import stdin


input = lambda: stdin.readline().rstrip()
cleaner = []


def spread():
    global arr

    dy = [0, -1, 0, 1]
    dx = [-1, 0, 1, 0]
    res = list([0] * C for _ in range(R))

    for cy in range(R):
        for cx in range(C):
            if arr[cy][cx] == -1:
                res[cy][cx] = -1
                continue

            if arr[cy][cx] == 0:
                continue

            dust = arr[cy][cx] // 5
            cnt = 0
            for i in range(4):
                ny, nx = cy + dy[i], cx + dx[i]
                if 0 <= ny < R and 0 <= nx < C and arr[ny][nx] != -1:
                    cnt += 1
                    res[ny][nx] += dust
            res[cy][cx] = arr[cy][cx] - dust * cnt
    arr = res[:]


def rotate(sy, sx, clockwise):
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    if not clockwise:
        dy = [1, 0, -1, 0]

    cy, cx, direc, ny, nx = sy, sx, 0, -1, -1
    while ny != cleaner[clockwise] or nx != 0:
        ny, nx = cy + dy[direc], cx + dx[direc]

        if (not clockwise and (ny < 0 or ny > sy)) \
                or (clockwise and (ny < sy or ny >= R)) \
                or nx < 0 or nx >= C:
            direc += 1
            continue

        arr[cy][cx] = arr[ny][nx]
        cy, cx = ny, nx

    arr[cy][cx] = 0
    arr[sy][0] = -1


if __name__ == "__main__":
    R, C, T = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(R)]

    for i in range(R):
        if arr[i][0] == -1:
            cleaner = [i, i + 1]
            break

    for _ in range(T):
        spread()
        rotate(cleaner[0], 0, 0)
        rotate(cleaner[1], 1, 1)

    ans = sum(map(sum, arr)) + 2
    print(ans)
