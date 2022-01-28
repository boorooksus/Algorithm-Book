from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 9)


n: int = 0
paper = []
dy = [0, 1, 0, 1]
dx = [0, 0, 1, 1]
res = [0, 0]


def input():
    return stdin.readline().strip()


def main():
    global n, paper, res
    n = int(input())

    for _ in range(n):
        paper.append(list(map(int, input().split())))

    divide(0, 0, n)
    print(res[0], res[1], sep='\n')


def divide(y: int, x: int, size: int) -> None:
    global n, paper, res

    for i in range(y, y + size):
        for j in range(x, x + size):
            if paper[y][x] != paper[i][j]:
                for k in range(4):
                    ny, nx = y + (size // 2) * dy[k], x + (size // 2) * dx[k]
                    divide(ny, nx, size // 2)
                return
    res[paper[y][x]] += 1
    return


if __name__ == '__main__':
    main()
