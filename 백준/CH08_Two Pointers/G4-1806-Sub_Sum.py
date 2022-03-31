from sys import stdin


INF = 1_000_000_001


if __name__ == "__main__":
    def input():
        return stdin.readline().rstrip()

    n, s = map(int, input().split())
    seq = list(map(int, input().split()))

    left, subsum, ans = 0, 0, INF
    for right in range(n):
        subsum += seq[right]

        while left <= right and subsum >= s:
            ans = min(right - left + 1, ans)
            subsum -= seq[left]
            left += 1

    print([0, ans][ans != INF])
