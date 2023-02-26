from sys import stdin
from collections import defaultdict
input = lambda: stdin.readline().rstrip()


def back_tracking(prefix: str) -> None:
    if len(prefix) == len(chars):
        print(prefix)
        return

    for char in visit:
        if visit[char]:
            visit[char] -= 1
            back_tracking(prefix + char)
            visit[char] += 1


if __name__ == "__main__":
    N = int(input())
    for _ in range(N):
        chars = sorted(list(input()))
        visit = defaultdict(int)
        for char in chars:
            visit[char] += 1
        back_tracking("")
