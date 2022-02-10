from sys import stdin
from collections import defaultdict


def back_tracking(chars, prefix: str, visit):
    if len(prefix) == len(chars):
        print(prefix)
        return

    for char in visit:
        if visit[char]:
            visit[char] -= 1
            back_tracking(chars, prefix + char, visit)
            visit[char] += 1


def main():
    def input():
        return stdin.readline().rstrip()

    n = int(input())
    for _ in range(n):
        x = sorted(input())
        visit = defaultdict(int)
        for char in x:
            visit[char] += 1
        back_tracking(x, '', visit)


if __name__ == "__main__":
    main()
