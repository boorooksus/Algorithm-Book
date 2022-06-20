from sys import stdin

input = lambda: stdin.readline().rstrip()

if __name__ == "__main__":
    R, C, Q = map(int, input().split())
    picture = [list(0 for _ in range(C + 1))] + \
              list([0] + list(map(int, input().split())) for _ in range(R))
    crds = list(list(map(int, input().split())) for _ in range(Q))

    for i in range(1, R + 1):
        for j in range(1, C + 1):
            picture[i][j] += picture[i - 1][j] + picture[i][j - 1] - picture[i - 1][j - 1]

    for a, b, c, d in crds:
        temp = picture[c][d] - picture[c][b - 1] - picture[a - 1][d] + picture[a - 1][b - 1]
        print(temp // ((c - a + 1) * (d - b + 1)))
