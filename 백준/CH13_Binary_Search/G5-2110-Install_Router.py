from sys import stdin
from typing import List


def binery_search(n: int, c: int, houses: List[int]) -> int:
    houses.sort()

    start, end = 1, houses[-1] - houses[0]
    res = 0
    while start <= end:
        mid = start + (end - start) // 2
        cnt, cur = 1, houses[0]

        for house in houses:
            if house >= cur + mid:
                cnt += 1
                cur = house

        if cnt >= c:
            res = mid
            start = mid + 1
        else:
            end = mid - 1

    return res


def main():
    def input():
        return stdin.readline().rstrip()

    n, c = map(int, input().split())
    houses = [int(input()) for _ in range(n)]

    print(binery_search(n, c, houses))


if __name__ == "__main__":
    main()
