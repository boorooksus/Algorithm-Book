from sys import stdin
from collections import deque
from typing import List
input = lambda: stdin.readline().rstrip()


def shuffle(cards: List[int], k: int) -> List[int]:
    cards, temp = deque(cards), deque()
    res = []
    for i in range(1, k + 2):
        for _ in range(2 ** (k - i + 1)):
            temp.appendleft(cards.pop())
        res = list(cards) + res
        cards, temp = temp, deque()
    return list(cards) + res


def sol() -> None:
    i = 1
    while 2 ** i < N:
        j = 1
        while 2 ** j < N:
            res = shuffle(shuffle(list(k for k in range(1, N + 1)), i), j)
            if res == arr:
                print(i, j)
                return
            j += 1
        i += 1


if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))
    sol()
