from sys import stdin
from typing import List


def dfs(seq: List[int], idx: int, n: int) -> str:
    for i in range(1, idx // 2 + 1):
        if seq[-2 * i:-i] == seq[-i:]:
            return ''

    if idx == n:
        return ''.join(map(str, seq))

    for i in range(1, 4):
        res = dfs(seq + [i], idx + 1, n)
        if res:
            return res


def main():
    n = int(stdin.readline())
    print(dfs([], 0, n))


if __name__ == "__main__":
    main()
