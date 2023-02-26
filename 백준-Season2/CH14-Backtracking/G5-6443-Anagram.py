from sys import stdin
from itertools import permutations
input = lambda: stdin.readline().rstrip()


if __name__ == "__main__":
    N = int(input())
    for _ in range(N):
        chars = list(input())
        visit = [False] * len(chars)
        res = set()
        for per in permutations(chars):
            res.add(''.join(per))
        print(*sorted(list(res)), sep='\n')


"""
시간 초과
순열을 이용한 풀이
"""