from sys import stdin
input = lambda: stdin.readline().rstrip()


def domino(y: int, x: int) -> None:
    global res

    while visit[y][x]:
        x += 1
        if x >= 7:
            y += 1
            if y == 8:
                res += 1
                return
            x = 0

    visit[y][x] = True

    if x + 1 < 7 and not used[arr[y][x]][arr[y][x + 1]]:
        a, b = arr[y][x], arr[y][x + 1]
        used[a][b] = True
        used[b][a] = True
        visit[y][x + 1] = True
        domino(y, x)
        visit[y][x + 1] = False
        used[a][b] = False
        used[b][a] = False

    if y + 1 < 8 and not used[arr[y][x]][arr[y + 1][x]]:
        a, b = arr[y][x], arr[y + 1][x]
        used[a][b] = True
        used[b][a] = True
        visit[y + 1][x] = True
        domino(y, x)
        visit[y + 1][x] = False
        used[a][b] = False
        used[b][a] = False

    visit[y][x] = False


if __name__ == "__main__":
    arr = list(list(map(int, input())) for _ in range(8))

    used = list([False] * 7 for _ in range(7))
    visit = list([False] * 7 for _ in range(8))
    res = 0
    domino(0, 0)
    print(res)
