from sys import stdin
from collections import defaultdict


if __name__ == "__main__":
    def input():
        return stdin.readline().rstrip()

    T = int(input())
    nums = [int(input()) for _ in range(T)]

    visit = defaultdict(bool)
    max_num = max(nums)
    for i in range(2, max_num):
        if visit[i]:
            continue
        j = 2
        while i * j < max_num * 2:
            visit[i * j] = True
            j += 1

    for num in nums:
        res = num
        while True:
            if not visit[res]:
                print(res)
                break
            res += 1

