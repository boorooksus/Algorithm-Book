from sys import stdin
from collections import Counter


input = lambda: stdin.readline().rstrip()


if __name__ == "__main__":
    N = int(input())
    files = [input() for _ in range(N)]

    cnts = Counter()
    for file in files:
        _, extension = file.split('.')
        cnts[extension] += 1

    for extension in sorted(cnts):
        print("%s %d" % (extension, cnts[extension]))

