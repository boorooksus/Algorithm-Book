"""
간단한 풀이
"""
from sys import stdin

def check(x):
    return x != x[::-1]


if __name__ == "__main__":
    word = list(stdin.readline().rstrip())

    if check(word):
        print(len(word))
    elif check(word[1:]):
        print(len(word) - 1)
    else:
        print(-1)
