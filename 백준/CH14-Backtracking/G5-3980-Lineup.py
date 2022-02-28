from sys import stdin
from typing import List


def back_tracking(players: List[List[int]], occupied, cur: int, stats: int) -> int:
    if cur == 11:
        return stats

    res = 0
    for i in range(11):
        if not occupied[i] and players[cur][i] != 0:
            occupied[i] = True
            res = max(back_tracking(players, occupied, cur + 1, stats + players[cur][i]),
                      res)
            occupied[i] = False
    return res


def main():
    def input():
        return stdin.readline().rstrip()

    c = int(input())
    for _ in range(c):
        players = [list(map(int, input().split())) for _ in range(11)]
        occupied = [False] * 11
        print(back_tracking(players, occupied, 0, 0))


if __name__ == "__main__":
    main()