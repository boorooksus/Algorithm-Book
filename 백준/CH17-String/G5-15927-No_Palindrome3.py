"""
통과
"""
from sys import stdin
from collections import Counter


def check(x):
    return x != x[::-1]


if __name__ == "__main__":
    word = list(stdin.readline().rstrip())

    cnt = Counter(word)
    if len(cnt.values()) == 1:
        print(-1)
        exit()

    for size in range(len(word), 1, -1):
        for start in range(len(word) - size + 1):
            if check(word[start:start + size]):
                print(size)
                exit()
    print(-1)
