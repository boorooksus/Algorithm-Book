from sys import stdin
from collections import defaultdict
input = lambda: stdin.readline().rstrip()


def get_gcd(a: int, b: int) -> int:
    if a > b:
        a, b = b, a

    if a == 0:
        return b
    if a == 1:
        return 1

    return get_gcd(a, b % a)


if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))
    X = int(input())

    dp = defaultdict(int)
    res = []
    for num in arr:
        if not dp[num]:
            dp[num] = get_gcd(num, X)
        if dp[num] == 1:
            res.append(num)

    print(sum(res) / len(res))
