from sys import stdin
from re import sub


def main():
    def input():
        return stdin.readline().rstrip()

    t = int(input())
    for _ in range(t):
        n = int(input())
        tels = [sub('[^0-9]', '', input()) for _ in range(n)]
        tels.sort()
        res = True
        for i in range(1, n):
            if tels[i - 1] == tels[i][:len(tels[i - 1])]:
                res = False
                break
        print(['NO', 'YES'][res])


if __name__ == "__main__":
    main()
