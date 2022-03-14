from sys import stdin


dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
arr = []
n, m = 0, 0


def rain(d: int, s: int, clouds):
    # 1. 모든 구름이 di 방향으로 si칸 이동
    for i, (y, x) in enumerate(clouds):
        ny, nx = (y + dy[d] * s) % n, (x + dx[d] * s) % n
        # 2. 비가 내려 바구니 물의 양이 1 증가
        arr[ny][nx] += 1
        clouds[i] = (ny, nx)

    # 3. 구름이 모두 사라진다
    # 4. 2에서 물이 증가한 칸 (r, c)에 물복사버그 마법을 시전
    ey = [-1, -1, 1, 1]
    ex = [-1, 1, 1, -1]
    for y, x in clouds:
        cnt = 0
        for i in range(4):
            ny, nx = y + ey[i], x + ex[i]
            if 0 <= ny < n and 0 <= nx < n and arr[ny][nx] > 0:
                cnt += 1
        arr[y][x] += cnt

    # 5. 물의 양이 2 이상인 칸에 구름이 생기고, 물의 양이 2 줄어든다
    new_clouds = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] >= 2 and (i, j) not in clouds:
                new_clouds.append((i, j))
                arr[i][j] -= 2

    return new_clouds


def main():
    def input():
        return stdin.readline().rstrip()
    global arr, n, m

    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    clouds = [(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)]
    for _ in range(m):
        d, s = map(int, input().split())
        clouds = rain(d, s, clouds)

    # 이동이 모두 끝난 후, 물의 양의 합을 구하기
    print(sum(sum(i) for i in arr))


if __name__ == "__main__":
    main()
