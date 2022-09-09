from sys import stdin
from typing import List
from collections import deque
input = lambda: stdin.readline().rstrip()


def shuffle(arr: List[int], k: int) -> List[int]:
    dq = deque(arr)
    cnt = 2 ** k
    dq.rotate(cnt)
    for i in range(2, k + 2):
        temp = deque()
        for _ in range(cnt):
            temp.append(dq.popleft())
        cnt = 2 ** (k - i + 1)
        temp.rotate(cnt)
        temp.extend(dq)
        dq = temp
    return list(dq)


if __name__ == "__main__":
    N = int(input())
    cards = list(map(int, input().split()))

    i = 1
    while 2 ** i < N:
        j = 1
        while 2 ** j < N:
            res = shuffle(shuffle(list(k for k in range(1, N + 1)), i), j)
            if res == cards:
                print(i, j)
                exit()
            j += 1
        i += 1
