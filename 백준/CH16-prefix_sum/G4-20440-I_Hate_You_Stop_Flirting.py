from sys import stdin
from collections import defaultdict

if __name__ == "__main__":
    def input():
        return stdin.readline().rstrip()


    N = int(input())
    mosquitos = [tuple(map(int, input().split())) for _ in range(N)]

    in_outs = defaultdict(int)
    for mos_in, mos_out in mosquitos:
        in_outs[mos_in] += 1
        in_outs[mos_out] -= 1

    max_mos, total = 0, 0
    times = sorted(list(in_outs.keys()))
    for time in times:
        total += in_outs[time]
        max_mos = max(total, max_mos)

    ans_start, ans_end = -1, -1
    total = 0
    for i, time in enumerate(times):
        total += in_outs[time]
        if not ~ans_start and total == max_mos:
            ans_start = time
        elif ~ans_start and total < max_mos:
            ans_end = time
            break

    print("%d\n%d %d" % (max_mos, ans_start, ans_end))
