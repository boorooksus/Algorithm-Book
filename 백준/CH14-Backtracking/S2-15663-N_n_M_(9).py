from sys import stdin
from collections import Counter


def back_tracking(cur):
    global cnts

    if len(cur) == m:
        print(*cur)

    for num in cnts:
        if cnts[num]:
            cnts[num] -= 1
            back_tracking(cur + [num])
            cnts[num] += 1


n, m = map(int, stdin.readline().split())
nums = sorted(list(map(int, stdin.readline().split())))
cnts = Counter(nums)
back_tracking([])

