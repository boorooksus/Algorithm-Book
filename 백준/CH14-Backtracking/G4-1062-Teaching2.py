"""
시간초과
"""
from sys import stdin
from collections import defaultdict


words = []
learned = defaultdict(bool)


def dfs(k: int) -> int:
    if k == 0:
        cnt = 0
        for word in words:
            for char in word:
                if not learned[char]:
                    break
            else:
                cnt += 1
        return cnt

    res = 0
    for i in range(ord('a'), ord('z') + 1):
        if not learned[chr(i)]:
            learned[chr(i)] = True
            res = max(dfs(k - 1), res)
            learned[chr(i)] = False

    return res


def main():
    def input():
        return stdin.readline().rstrip()
    global words

    n, k = map(int, input().split())
    words = [input()[4:-4] for _ in range(n)]

    if k < 5:
        print(0)
        return

    elif k == 26:
        print(n)
        return

    for char in "antic":
        learned[char] = True
        k -= 1

    print(dfs(k))


if __name__ == "__main__":
    main()
