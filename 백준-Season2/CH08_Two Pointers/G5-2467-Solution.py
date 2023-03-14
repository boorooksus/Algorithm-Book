from sys import stdin
input = lambda:stdin.readline().rstrip()


MAX = 2_000_000_000


if __name__ == "__main__":
    N = int(input())
    sols = list(map(int, input().split()))

    sols.sort()
    left, right = 0, N - 1
    ans = [MAX, 0, 0]
    while left < right:
        res = sols[left] + sols[right]
        if abs(res) < abs(ans[0]):
            ans = [res, sols[left], sols[right]]

        if res < 0:
            left += 1
        elif res > 0:
            right -= 1
        else:
            break

    print(ans[1], ans[2])
