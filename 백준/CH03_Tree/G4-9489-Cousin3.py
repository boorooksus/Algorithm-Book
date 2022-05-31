"""
코드 개선
"""
from sys import stdin
from collections import defaultdict


input = lambda: stdin.readline().rstrip()


if __name__ == "__main__":
    while True:
        n, k = map(int, input().split())

        if n == 0 and k == 0:
            break
        nums = list(map(int, input().split()))

        parents = defaultdict(int)
        target = nums.index(k)
        parent, cur = 0, 1
        while cur < n:
            while cur + 1 < n and nums[cur] + 1 == nums[cur + 1]:
                parents[cur] = parent
                cur += 1
            parents[cur] = parent
            cur += 1
            parent += 1

        if not parents[target]:
            print(0)
            continue

        ans = 0
        for i in range(2, n):
            if parents[i] and parents[i] != parents[target] and parents[parents[i]] == parents[parents[target]]:
                ans += 1
        print(ans)
