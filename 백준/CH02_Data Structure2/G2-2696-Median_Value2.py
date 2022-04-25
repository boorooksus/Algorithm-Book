from sys import stdin
from heapq import heappop, heappush


def get_median() -> None:
    mid = nums[0]
    left, right, ans = [], [], [mid]
    for i, num in enumerate(nums[1:], 1):
        if num < mid:
            heappush(left, -num)
        else:
            heappush(right, num)

        if i % 2 == 0:
            if len(left) > len(right):
                heappush(right, mid)
                mid = -heappop(left)
            elif len(left) < len(right):
                heappush(left, -mid)
                mid = heappop(right)
            ans.append(mid)

    print(len(ans))
    for i, num in enumerate(ans):
        if i != 0 and i % 10 == 0:
            print()
        print(num, end=' ')
    print()


if __name__ == "__main__":
    def input():
        return stdin.readline().rstrip()

    T = int(input())
    for _ in range(T):
        M = int(input())
        nums = []
        for _ in range((M - 1) // 10 + 1):
            nums += list(map(int, input().split()))

        get_median()

