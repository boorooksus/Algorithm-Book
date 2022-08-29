from sys import stdin
input = lambda: stdin.readline().rstrip()


if __name__ == "__main__":
    N = int(input())
    villages = list(list(map(int, input().split())) for _ in range(N))

    people = sum(villages[i][1] for i in range(N))
    cnt = 0
    for x, a in sorted(villages):
        cnt += a
        if cnt > (people // 2):
            print(x)
            break
