"""
시간초과
"""
from sys import stdin
from heapq import heappop, heappush
from collections import defaultdict


class Problems:
    def __init__(self):
        self.easy = []
        self.hard = []
        self.lg = defaultdict(list)

    def add(self, p: int, l: int, g: int) -> None:
        heappush(self.easy, (l, g, p))
        heappush(self.hard, (-l, -g, p))
        self.lg[p] = [l, g]

    def solved(self, p: int) -> None:
        self.lg[p] = []

    def recommend(self, g, x) -> int:
        if x == 1:
            temp = []
            while self.hard:
                level, category, problem = heappop(self.hard)
                if self.lg[problem] and -level == self.lg[problem][0] \
                        and -category == self.lg[problem][1]:
                    temp.append((level, category, problem))
                    if -category == g:
                        for item in temp:
                            heappush(self.hard, item)
                        return problem
        else:
            temp = []
            while self.easy:
                level, category, problem = heappop(self.easy)
                if self.lg[problem] and \
                        level == self.lg[problem][0] and category == self.lg[problem][1]:
                    temp.append((level, category, problem))
                    if category == g:
                        for item in temp:
                            heappush(self.easy, item)
                        return problem

    def recommend2(self, x: int) -> int:
        if x == 1:
            while not self.lg[self.easy[0][2]] or -self.hard[0][0] != self.lg[self.hard[0][2]][0] or \
                    -self.hard[0][1] != self.lg[self.hard[0][2]][1]:
                heappop(self.hard)
            return self.hard[0][2]
        else:
            while not self.lg[self.easy[0][2]] or self.easy[0][0] != self.lg[self.easy[0][2]][0] or \
                    self.easy[0][1] != self.lg[self.easy[0][2]][1]:
                heappop(self.easy)
            return self.easy[0][2]

    def recommend3(self, x: int, l: int) -> int:
        if x == 1:
            temp = []
            while self.hard and -self.hard[0][0] >= l:
                level, category, problem = heappop(self.hard)
                if self.lg[problem] and self.lg[problem][0] == -level \
                        and self.lg[problem][1] == -category:
                    temp.append((level, category, problem))

            for item in temp:
                heappush(self.hard, item)
            return temp[-1][2] if temp else -1
        else:
            temp = []
            while self.easy and self.easy[0][0] <= l:
                level, category, problem = heappop(self.easy)
                if self.lg[problem] and self.lg[problem][0] == level \
                        and self.lg[problem][1] == category:
                    temp.append((level, category, problem))

            for item in temp:
                heappush(self.easy, item)
            return temp[-1][2] if temp else -1


def main():
    def input():
        return stdin.readline().rstrip()

    problems = Problems()
    n = int(input())
    for _ in range(n):
        p, l, g = map(int, input().split())
        problems.add(p, l, g)

    m = int(input())
    for _ in range(m):
        cmd = list(input().split())

        if cmd[0] == 'add':
            problems.add(int(cmd[1]), int(cmd[2]), int(cmd[3]))
        elif cmd[0] == 'solved':
            problems.solved(int(cmd[1]))
        elif cmd[0] == 'recommend':
            print(problems.recommend(int(cmd[1]), int(cmd[2])))
        elif cmd[0] == 'recommend2':
            print(problems.recommend2(int(cmd[1])))
        elif cmd[0] == 'recommend3':
            print(problems.recommend3(int(cmd[1]), int(cmd[2])))


if __name__ == "__main__":
    main()
