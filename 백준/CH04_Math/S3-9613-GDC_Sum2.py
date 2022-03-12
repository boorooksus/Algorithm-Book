from sys import stdin
from itertools import combinations
from math import gcd


def main():
    t = int(stdin.readline())
    for _ in range(t):
        nums = list(map(int, stdin.readline().split()))

        res = 0
        combs = combinations(nums[1:], 2)
        for a, b in combs:
            res += gcd(a, b)

        print(res)


if __name__ == "__main__":
    main()
