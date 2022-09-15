from sys import stdin
input = lambda: stdin.readline().rstrip()

"""
direction
   N: 0,
W: 3    E: 1
   S: 2
"""

rotate = {
    0: [(0, -1, 3), (1, 0, 2), (0, 1, 1), (-1, 0, 0)],  # w s e n
    1: [(-1, 0, 0), (0, -1, 3), (1, 0, 2), (0, 1, 1)],  # n w s e
    2: [(0, 1, 1), (-1, 0, 0), (0, -1, 3), (1, 0, 2)],  # e n w s
    3: [(1, 0, 2), (0, 1, 1), (-1, 0, 0), (0, -1, 3)]  # s e n w
}

back = {
    0: (1, 0, 0), 1: (0, -1, 1), 2: (-1, 0, 2), 3: (0, 1, 3)
}


def dfs(sy: int, sx: int, direction: int, cnt: int) -> int:

    # print(sy, sx, direction)

    if not arr[sy][sx]:
        arr[sy][sx] = 2
        cnt += 1

    for i in range(4):
        dy, dx, dr = rotate[direction][i]
        ny, nx = sy + dy, sx + dx
        if 0 <= ny < N and 0 <= nx < M and not arr[ny][nx]:
            return dfs(ny, nx, dr, cnt)

    dy, dx, dr = back[direction]
    ny, nx = sy + dy, sx + dx
    if 0 <= ny < N and 0 <= nx < M and arr[ny][nx] != 1:
        return dfs(ny, nx, dr, cnt)

    return cnt


if __name__ == "__main__":
    N, M = map(int, input().split())
    r, c, d = map(int, input().split())
    arr = list(list(map(int, input().split())) for _ in range(N))

    print(dfs(r, c, d, 0))
