from sys import stdin
input = lambda: stdin.readline().rstrip()


def get_cnt(dist: int) -> int:
    cnt, cur = 1, x[0]
    for loc in x:
        if cur + dist <= loc:
            cnt += 1
            cur = loc

    return cnt


if __name__ == "__main__":
    N, C = map(int, input().split())
    x = sorted(list(int(input()) for _ in range(N)))

    left, right = 1, x[-1] - x[0]
    ans = 0
    while left <= right:
        mid = left + (right - left) // 2
        cnt = get_cnt(mid)
        if cnt < C:
            right = mid - 1
        else:
            ans = mid
            left = mid + 1

    print(ans)
