from sys import stdin
from typing import List
import heapq

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]


def get_place(friends: List[int]) -> List[int]:
    hq = []

    for row in range(n):
        for col in range(n):
            if place[row][col] != 0:
                continue

            favorite, empty = 0, 0

            for i in range(4):
                ny, nx = row + dy[i], col + dx[i]

                if 0 <= ny < n and 0 <= nx < n:
                    if place[ny][nx] == 0:
                        empty += 1
                    elif place[ny][nx] in friends:
                        favorite += 1

            heapq.heappush(hq, [-favorite, -empty, row, col])

    result = heapq.heappop(hq)
    return [result[2], result[3]]


def get_score() -> int:
    total = 0
    for row in range(n):
        for col in range(n):
            cnt = 0
            for i in range(4):
                ny, nx = row + dy[i], col + dx[i]
                if 0 <= ny < n and 0 <= nx < n and\
                    place[ny][nx] in friends[place[row][col]]:
                    cnt += 1

            total += 10 ** (cnt - 1) if cnt > 0 else 0
    return total


n = int(stdin.readline())
place = [[0 for _ in range(n)] for _ in range(n)]
friends = {}
for i in range(n ** 2):
    temp = list(map(int, stdin.readline().split()))
    friends[temp[0]] = temp[1:]
    row, col = get_place(temp)
    place[row][col] = temp[0]

print(get_score())


