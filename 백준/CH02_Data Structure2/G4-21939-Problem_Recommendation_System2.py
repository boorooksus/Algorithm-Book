"""
heapq 이용
"""

from sys import stdin
from collections import defaultdict
import heapq


class Problems:
    def __init__(self):
        self.in_list = defaultdict(bool)
        self.easy = []
        self.hard = []

    def recommend(self, x) -> int:
        if x == 1:
            while not self.in_list[-self.hard[0][1]]:
                heapq.heappop(self.hard)
            return -self.hard[0][1]
        else:
            while not self.in_list[self.easy[0][1]]:
                heapq.heappop(self.easy)
            return self.easy[0][1]

    def add(self, p, l) -> None:
        while self.easy and not self.in_list[self.easy[0][1]]:
            heapq.heappop(self.easy)
        while self.hard and not self.in_list[-self.hard[0][1]]:
            heapq.heappop(self.hard)
        self.in_list[p] = True
        heapq.heappush(self.easy, (l, p))
        heapq.heappush(self.hard, (-l, -p))

    def solved(self, p) -> None:
        self.in_list[p] = False

def main():
    def input():
        return stdin.readline().rstrip()

    prob = Problems()
    n = int(input())
    for _ in range(n):
        p, l = map(int, input().split())
        prob.add(p, l)
    m = int(input())
    for _ in range(m):
        cmd = list(input().split())
        if cmd[0] == 'add':
            prob.add(int(cmd[1]), int(cmd[2]))
        elif cmd[0] == 'recommend':
            print(prob.recommend(int(cmd[1])))
        else:
            prob.solved(int(cmd[1]))


if __name__ == "__main__":
    main()
