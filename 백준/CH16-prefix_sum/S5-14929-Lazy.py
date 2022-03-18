"""
시간초과
"""
from sys import stdin


def main():
    def input():
        return stdin.readline().rstrip()

    n = int(input())
    nums = list(map(int, input().split()))

    res = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            res += nums[i] * nums[j]

    print(res)


if __name__ == "__main__":
    main()
    