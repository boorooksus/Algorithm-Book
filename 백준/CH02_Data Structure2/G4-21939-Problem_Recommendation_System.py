"""
python3 시간초과, pypy3 통과
"""

from sys import stdin
from collections import defaultdict


class Problems:
    def __init__(self):
        self.levels = defaultdict(list)
        self.problems = {}

    def recommend(self, x) -> int:
        if x == 1:
            return max(self.levels[max(self.levels.keys())])
        else:
            return min(self.levels[min(self.levels.keys())])

    def add(self, p, l) -> None:
        if p in self.problems:
            self.levels[self.problems[p]].remove(p)
        self.problems[p] = l
        self.levels[l].append(p)

    def solved(self, p) -> None:
        self.levels[self.problems[p]].remove(p)
        if not self.levels[self.problems[p]]:
            self.levels.pop(self.problems[p])
        self.problems.pop(p)


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
