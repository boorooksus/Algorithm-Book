from sys import stdin
inpout = lambda: stdin.readline().rstrip()


# ===== 1 =====
direction = {0: 'N', 1: 'E', 2: 'S', 3: 'W'}
move = {'N': (-1, 0), 'E': (0, 1), 'S': (1, 0), 'W': (0, -1)}
order = {
    'N': ['W', 'S', 'E', 'N'],
    'E': ['N', 'W', 'S', 'E'],
    'S': ['E', 'N', 'W', 'S'],
    'W': ['S', 'E', 'N', 'W']
}
back = {'N': (1, 0), 'E': (0, -1), 'S': (-1, 0), 'W': (0, 1)}

if __name__ == "__main__":
    N, M = map(int, input().split())
    r, c, d = map(int, input().split())
    arr = list(list(map(int, input().split())) for _ in range(N))

    cnt = 0
    d = direction[d]
    while True:
        if arr[r][c] == 0:
            arr[r][c] = 2
            cnt += 1

        for next_dir in order[d]:
            dy, dx = move[next_dir]
            ny, nx = r + dy, c + dx

            if 0 <= ny < N and 0 <= nx < M and not arr[ny][nx]:
                r, c, d = ny, nx, next_dir
                break

        else:
            dy, dx = back[d]
            ny, nx = r + dy, c + dx
            # ===== 2 =====
            if ny < 0 or ny >= N or nx < 0 or nx >= M \
                    or arr[ny][nx] == 1:
                break

            r, c = ny, nx

    print(cnt)


"""
1: 좌표 매핑 시, 정확하게 할 것 주의. 헷갈릴 수 있으므로 되도록 적게 사용할 것
2: 조건문 and, or, 범위 주의. 범위 내의 값인지 밖의 값인지 조건 주의깊게 생각하기
"""