from sys import stdin
from heapq import heappush, heappop
input = lambda: stdin.readline().rstrip()


def runner(k: int) -> None:
    for i in range(k):
        operation, num = input().split()
        num = int(num)

        if operation == 'I':
            heappush(hq_min, (num, i))
            heappush(hq_max, (-num, i))
            exist[i] = True

        elif num == 1:
            while hq_max and not exist[hq_max[0][1]]:
                heappop(hq_max)
            if hq_max:
                val, idx = heappop(hq_max)
                exist[idx] = False

        else:
            while hq_min and not exist[hq_min[0][1]]:
                heappop(hq_min)
            if hq_min:
                val, idx = heappop(hq_min)
                exist[idx] = False


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        hq_min = []
        hq_max = []
        exist = [False] * 1_000_000

        k = int(input())
        runner(k)

        while hq_max and not exist[hq_max[0][1]]:
            heappop(hq_max)
        while hq_min and not exist[hq_min[0][1]]:
            heappop(hq_min)

        if hq_min and hq_max:
            print(-hq_max[0][0], hq_min[0][0])
        else:
            print("EMPTY")
