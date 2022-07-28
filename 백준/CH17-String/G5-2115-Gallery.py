from sys import stdin
input = lambda: stdin.readline().rstrip()


if __name__ == "__main__":
    M, N = map(int, input().split())
    arr = [list(input()) for _ in range(M)]

    ans = 0
    visit = [list([False] * 4 for _ in range(N)) for _ in range(M)]
    for y in range(1, M - 1):
        for x in range(1, N - 1):
            if arr[y][x] == '.' and arr[y][x + 1] == '.':
                if not visit[y][x][0] and arr[y - 1][x] == 'X' and arr[y - 1][x + 1] == 'X':
                    ans += 1
                    visit[y][x][0], visit[y][x + 1][0] = True, True
                if not visit[y][x][1] and arr[y + 1][x] == 'X' and arr[y + 1][x + 1] == 'X':
                    ans += 1
                    visit[y][x][1], visit[y][x + 1][1] = True, True
            if arr[y][x] == '.' and arr[y + 1][x] == '.':
                if not visit[y][x][2] and arr[y][x - 1] == 'X' and arr[y + 1][x - 1] == 'X':
                    ans += 1
                    visit[y][x][2], visit[y + 1][x][2] = True, True
                if not visit[y][x][3] and arr[y][x + 1] == 'X' and arr[y + 1][x + 1] == 'X':
                    ans += 1
                    visit[y][x][3], visit[y + 1][x][3] = True, True

    print(ans)
