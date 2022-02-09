from sys import stdin
from collections import deque


def main():
    def input():
        return stdin.readline().rstrip()

    n, k = map(int, input().split())
    durab = deque(map(int, input().split()))
    robots = deque([False] * 2 * n)
    up, down = 0, n - 1

    step = 0
    while k > 0:
        step += 1

        # rotate belt
        durab.rotate(1)
        robots.rotate(1)
        robots[n - 1] = False

        # move robots
        if any(robots):
            for i in range(n - 1, 0, -1):
                if durab[i] > 0 and not robots[i] and robots[i - 1]:
                    robots[i], robots[i - 1] = True, False
                    durab[i] -= 1
                    if not durab[i]:
                        k -= 1
                    if i == n - 1:
                        robots[i] = False

        # put new robot on the belt
        if durab[0] > 0:
            robots[0] = True
            durab[0] -= 1
            if not durab[0]:
                k -= 1

    print(step)


if __name__ == "__main__":
    main()
