from sys import stdin
from itertools import combinations
from collections import defaultdict


input = lambda: stdin.readline().rstrip()


def get_dist(a, b) -> int:
    return abs(a // 100 - b // 100) + abs(a % 100 - b % 100)


if __name__ == "__main__":
    N, M = map(int, input().split())
    city = list(list(map(int, input().split())) for _ in range(N))

    houses, chickens = [], []
    for i in range(N):
        for j in range(N):
            if city[i][j] == 1:
                houses.append(i * 100 + j)
            elif city[i][j] == 2:
                chickens.append(i * 100 + j)

    dists = defaultdict(dict)
    for house in houses:
        for chicken in chickens:
            dists[house][chicken] = get_dist(house, chicken)

    ans = 10000
    for comb in combinations(chickens, M):
        dist = 0
        for house in houses:
            temp = 10000
            for chicken in comb:
                temp = min(dists[house][chicken], temp)
            dist += temp
        ans = min(dist, ans)
    print(ans)