from sys import stdin
import heapq


def runner(k: int) -> None:
    hq_min, hq_max = [], []
    exist = [False for _ in range(k)]

    for i in range(k):
        letter, num_str = stdin.readline().split()
        num = int(num_str)

        if letter == "I":
            heapq.heappush(hq_min, (num, i))
            heapq.heappush(hq_max, (-num, i))
            exist[i] = True

        elif num == 1:
            while hq_max and not exist[hq_max[0][1]]:
                heapq.heappop(hq_max)
            if hq_max:
                exist[hq_max[0][1]] = False
                heapq.heappop(hq_max)

        else:
            while hq_min and not exist[hq_min[0][1]]:
                heapq.heappop(hq_min)
            if hq_min:
                exist[hq_min[0][1]] = False
                heapq.heappop(hq_min)

    while hq_max and not exist[hq_max[0][1]]:
        heapq.heappop(hq_max)
    while hq_min and not exist[hq_min[0][1]]:
        heapq.heappop(hq_min)
    if hq_max and hq_min:
        print(-hq_max[0][0], hq_min[0][0])
    else:
        print('EMPTY')


t = int(stdin.readline())
for _ in range(t):
    k = int(stdin.readline())
    runner(k)
