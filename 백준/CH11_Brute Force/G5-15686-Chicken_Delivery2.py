"""
코드 수 줄인 방법
"""
from sys import stdin
from itertools import combinations


input = lambda: stdin.readline().rstrip()


if __name__ == "__main__":
    N, M = map(int, input().split())
    city = list(list(map(int, input().split())) for _ in range(N))

    houses, chickens = [], []
    for i in range(N):
        for j in range(N):
            if city[i][j] == 1:
                houses.append((i, j))
            elif city[i][j] == 2:
                chickens.append((i, j))

    ans = 10000
    for comb in combinations(chickens, M):
        dist = 0
        for house in houses:
            temp = 10000
            for i in range(M):
                temp = min(abs(house[0] - comb[i][0]) + abs(house[1] - comb[i][1]), temp)
            dist += temp
        ans = min(dist, ans)
    print(ans)
