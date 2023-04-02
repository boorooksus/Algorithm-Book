from sys import stdin
input = lambda: stdin.readline().rstrip()


if __name__ == "__main__":
    N = int(input())
    arr = list(tuple(map(int, input().split())) for _ in range(N))

    total = sum(i[1] for i in arr)
    cnt = 0
    for x, a in sorted(arr):
        cnt += a
        if cnt > total // 2:
            print(x)
            break
