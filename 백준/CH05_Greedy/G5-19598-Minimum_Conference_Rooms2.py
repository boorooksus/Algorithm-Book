"""
참고: https://jminie.tistory.com/7
"""
from sys import stdin


def main():
    def input():
        return stdin.readline().rstrip()

    n = int(input())
    times = []
    for _ in range(n):
        start, end = map(int, input().split())
        times += [[start, 1], [end, -1]]
    times.sort()

    cnt, res = 0, 0
    for _, flag in times:
        cnt += flag
        res = max(cnt, res)
    print(res)


if __name__ == "__main__":
    main()
