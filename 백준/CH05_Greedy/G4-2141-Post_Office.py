from sys import stdin, maxsize


if __name__ == "__main__":
    def input():
        return stdin.readline().rstrip()

    N = int(input())
    villages = [tuple(map(int, input().split())) for _ in range(N)]

    villages.sort(key=lambda x: x[0], reverse=True)
    mid = sum(a for _, a in villages) // 2

    cnt = 0
    for a, x in villages:
        cnt += x

        if cnt > mid:
            print(a)
            break
