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
        parent, cur, target = 0, 1, -1
        while cur < n:
            while cur < n and \
                    (not children[parent] or nums[cur - 1] + 1 == nums[cur]):
                children[parent].append(cur)
                parents[cur] = parent
                if nums[cur] == k:
                    target = parent
                cur += 1
            parent += 1

        if target <= 0:
            print(0)
            continue

        ans = 0
        for parent in children[parents[target]]:
            if parent == target:
                continue
            ans += len(children[parent])
        print(ans)
