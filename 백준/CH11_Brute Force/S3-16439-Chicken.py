from sys import stdin
from itertools import combinations


if __name__ == "__main__":
    def input():
        return stdin.readline().rstrip()

    n, m = map(int, input().split())
    scores = [list(map(int, input().split())) for _ in range(n)]

    ans = 0
    for comb in combinations(list(i for i in range(m)), 3):
        res = 0

        for i in range(n):
            res += max(scores[i][comb[0]], scores[i][comb[1]], scores[i][comb[2]])
        ans = max(res, ans)

    print(ans)

