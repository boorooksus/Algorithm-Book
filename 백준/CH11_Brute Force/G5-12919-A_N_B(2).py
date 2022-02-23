"""
시간 초과
"""

from sys import stdin


def dfs(s, t) -> int:
    if len(s) == len(t):
        return [0, 1][s == t]

    op1 = dfs(s + 'A', t)
    op2 = dfs('B' + s[::-1], t)

    return op1 or op2


def main():
    S = stdin.readline().rstrip()
    T = stdin.readline().rstrip()
    print(dfs(S, T))


if __name__ == "__main__":
    main()
