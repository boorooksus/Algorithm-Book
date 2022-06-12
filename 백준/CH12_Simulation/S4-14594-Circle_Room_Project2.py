"""
좀 더 쉬운 풀이
"""
from sys import stdin


input = lambda: stdin.readline().rstrip()


if __name__ == "__main__":
    N, M = (int(input()) for _ in range(2))
    rooms = [0] * N
    for i in range(M):
        x, y = map(int, input().split())
        for j in range(x, y):
            rooms[j - 1] = 1
    print(rooms.count(0))
