"""
KMP 알고리즘
"""

from sys import stdin
from typing import List


def make_table(p: str) -> List[int]:
    table = [0] * len(p)

    j = 0
    for i in range(1, len(table)):
        while j > 0 and p[i] != p[j]:
            j = table[j - 1]

        if p[i] == p[j]:
            j += 1
            table[i] = j

    return table


def kmp(s: str, p: str, table: List[int]) -> bool:
    i, j = 0, 0

    for i in range(len(s)):
        while j > 0 and s[i] != p[j]:
            j = table[j - 1]

        if s[i] == p[j]:
            j += 1
            if j == len(p):
                return True

    return False


def main():
    s = stdin.readline().rstrip()
    p = stdin.readline().rstrip()

    table = make_table(p)
    print([0, 1][kmp(s, p, table)])


if __name__ == "__main__":
    main()
