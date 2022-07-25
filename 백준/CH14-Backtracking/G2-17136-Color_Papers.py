"""
틀림
"""
from sys import stdin
input = lambda: stdin.readline().rstrip()


def check(sy: int, sx: int, paper: int, flag: int) -> bool:
    if not papers[paper]:
        return False
    for y in range(sy, sy + paper):
        for x in range(sx, sx + paper):
            if y >= 10 or x >= 10 or arr[y][x] == 0:
                for py in range(sy, sy + paper):
                    for px in range(sx, sx + paper):
                        if py >= 10 or px >= 10 or arr[py][px] == 0:
                            return False
                        arr[py][px] = 1
                return False
            arr[y][x] = flag
    papers[paper] -= 1
    return True


def dfs(y: int, x: int, cnt: int) -> int:
    while y < 10 and (x >= 10 or arr[y][x] != 1):
        x += 1
        if x >= 10:
            y += 1
            x = 0

    if y == 10:
        return cnt

    if y == 3 and x == 3:
        here = 0
    for i in range(4, 0, -1):
        if check(y, x, i, 2):
            res = dfs(y, x + i, cnt + 1)
            if res != -1:
                return res
        check(y, x, i, 1)
    return -1


if __name__ == "__main__":
    arr = list(list(map(int, input().split())) for _ in range(10))

    papers = {i: 5 for i in range(1, 5)}
    print(dfs(0, 0, 0))
