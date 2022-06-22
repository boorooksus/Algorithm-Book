"""
시간 초과
"""
from sys import stdin


def check(x):
    return x != x[::-1]


if __name__ == "__main__":
    word = stdin.readline().rstrip()

    for size in range(len(word), 1, -1):
        for start in range(len(word) - size + 1):
            if check(word[start:start + size]):
                print(size)
                exit()
    print(-1)
