from sys import stdin
from collections import deque


def main():
    def input():
        return stdin.readline().rstrip()

    M, N, H = map(int, input().split())
    box = []
    unriped = 0
    dq = deque()

    for i in range(H):
        layer = []
        for j in range(N):
            layer.append(list(map(int, input().split())))
            for k in range(M):
                if layer[j][k] == 0:
                    unriped += 1
                elif layer[j][k] == 1:
                    dq.append((i, j, k, 1))
        box.append(layer)

    dz = [1, 0, 0, 0, 0, -1]
    dy = [0, 1, -1, 0, 0, 0]
    dx = [0, 0, 0, 1, -1, 0]
    res = 0
    while unriped > 0 and dq:
        cz, cy, cx, res = dq.popleft()
        for i in range(6):
            nz, ny, nx = cz + dz[i], cy + dy[i], cx + dx[i]
            if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M \
                    and box[nz][ny][nx] == 0:
                unriped -= 1
                dq.append((nz, ny, nx, res + 1))
                box[nz][ny][nx] = 1

    if not dq:
        res = -1

    print(res)


if __name__ == "__main__":
    main()
