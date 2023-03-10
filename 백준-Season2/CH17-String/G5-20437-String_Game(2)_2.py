from sys import stdin
from collections import defaultdict
input = lambda: stdin.readline().rstrip()


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        W = input()
        K = int(input())

        ans = [10000, 0]

        indices = defaultdict(list)
        for i, char in enumerate(W):
            indices[char].append(i)

            if len(indices[char]) >= K:
                ans[0] = min(ans[0], i - indices[char][-K] + 1)
                ans[1] = max(ans[1], i - indices[char][-K] + 1)

        if ans[0] == 10000 and ans[1] == 0:
            print(-1)
        else:
            print(*ans, sep=' ')

"""
더 간략한 풀이
"""