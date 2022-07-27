from sys import stdin
input = lambda: stdin.readline().rstrip()


if __name__ == "__main__":
    L, W, H = map(int, input().split())
    n = int(input())
    cubes = list(list(map(int, input().split())) for _ in range(n))

    cubes.sort(reverse=True)
    prev, ans = 0, 0

    for n, cnt in cubes:
        prev <<= 3
        v = 2 ** n
        max_cnt = min(cnt, (L // v) * (W // v) * (H // v) - prev)
        ans += max_cnt
        prev += max_cnt

    print([-1, ans][prev == L * W * H])
