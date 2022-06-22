"""
시간 초과
"""
from sys import stdin


def check(x, start, end):
    while start < end:
        if x[start] != x[end]:
            return True
        start += 1
        end -= 1
    return False


if __name__ == "__main__":
    word = stdin.readline().rstrip()

    for size in range(len(word), 1, -1):
        for start in range(len(word) - size + 1):
            if check(word, start, start + size - 1):
                print(size)
                exit()
    print(-1)
