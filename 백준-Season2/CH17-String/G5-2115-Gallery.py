from sys import stdin
input = lambda: stdin.readline().rstrip()


def dfs(y: int, x: int, d: int) -> int:
    if arr[y][x] == 'X':
        return 0

    ny, nx = y + dy[d], x + dx[d]
    if arr[ny][nx] == 'X' and not visit[y][x] & (1 << d):
        visit[y][x] |= (1 << d)
        return 1
    return 0


if __name__ == "__main__":
    M, N = map(int, input().split())
    arr = [list(input()) for _ in range(M)]

    # 방에서 벽 탐색 방향 (상 우 하 좌)
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    # 빈 방의 각 방향의 벽에서 그림 걸려 있는지 여부를 4비트로 저장 (상 우 하 좌)
    # 빈 방의 좌측 벽과 상측 벽에 그림이 있다면 '1001'이 저장
    visit = [[0] * N for _ in range(M)]

    ans = 0
    for r in range(1, M - 1):
        for c in range(1, N - 1):
            if arr[r][c] == '.':
                # 빈 방에서 상하좌우가 벽인지 탐색
                for i in range(4):
                    ny, nx = r + dy[i], c + dx[i]
                    if arr[ny][nx] == 'X' and not visit[r][c] & (1 << i):
                        # 그림이 없는 벽인 경우
                        visit[r][c] |= (1 << i)
                        # 옆칸까지 그림을 모두 걸 수 있는지 확인
                        # 빈방에서 벽을 바라보는 방향이 상 또는 하 인경우 우측칸을,
                        #   좌 또는 우 인경우 아래측 칸을 탐색
                        ans += dfs(r + abs(dx[i]), c + abs(dy[i]), i)

    print(ans)


"""
dfs, 비트 연산
"""