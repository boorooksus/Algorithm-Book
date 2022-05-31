"""
틀림
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

        parents, children = defaultdict(int), defaultdict(list)
        parents[0] = -1
        children[-1].append(0)

        grand, cur, target = -1, 1, -2
        while cur < n:
            for parent in children[grand]:
                while cur < n and \
                        (not children[parent] or nums[cur - 1] + 1 == nums[cur]):
                    children[parent].append(cur)
                    parents[cur] = parent
                    if nums[cur] == k:
                        target = parent
                    cur += 1
            if target != -2:
                break
            grand += 1

        if target <= 0:
            print(0)
            break

        ans = 0
        for parent in children[parents[target]]:
            if parent == target:
                continue
            ans += len(children[parent])
        print(ans)
