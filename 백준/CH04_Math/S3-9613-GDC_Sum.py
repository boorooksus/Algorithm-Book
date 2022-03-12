from sys import stdin
from itertools import combinations
from collections import defaultdict
from typing import List


denominators = defaultdict(list)


def get_denominator(a: int) -> List[int]:
    if not denominators[a]:
        for i in range(1, int(a ** 0.5) + 1):
            if a % i == 0:
                denominators[a] += [i, a // i]

    return denominators[a]


def get_gcd(a: int, b: int) -> int:
    if b % a == 0:
        return a
    x, y = get_denominator(a), get_denominator(b)
    x.sort(reverse=True)
    for num in x:
        if num in y:
            return num


def main():
    t = int(stdin.readline())
    for _ in range(t):
        nums = list(map(int, stdin.readline().split()))

        res = 0
        combs = combinations(sorted(nums[1:]), 2)
        for a, b in combs:
            res += get_gcd(a, b)
        print(res)


if __name__ == "__main__":
    main()
