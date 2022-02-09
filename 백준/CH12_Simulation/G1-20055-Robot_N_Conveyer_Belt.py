"""
python3: 시간초과, pypy3: 런타임에러
"""

from sys import stdin


n, k = 0, 0
durab = []
robots = []


def rotate_belt(up: int, down: int) -> tuple[int, int]:
    if robots[(down - 1) % (2 * n)]:
        robots[(down - 1) % (2 * n)] = False

    return (up - 1) % (2 * n), (down - 1) % (2 * n)


def move_robots(up: int, down: int):
    global k

    i = down
    while i != up:
        if durab[i] > 0 and not robots[i] and robots[(i - 1) % (2 * n)]:
            robots[(i - 1) % (2 * n)], robots[i] = False, True
            durab[i] -= 1
            if i == down:
                robots[i] = False

            if durab[i] == 0:
                k -= 1
        i = (i - 1) % (2 * n)


def put_robot(up: int):
    global k

    if durab[up] > 0:
        robots[up] = True
        durab[up] -= 1

        if durab[up] == 0:
            k -= 1


def main():
    def input():
        return stdin.readline().rstrip()
    global n, k, durab, robots

    n, k = map(int, input().split())
    durab = list(map(int, input().split()))
    robots = [False] * 2 * n
    up, down = 0, n - 1

    step = 0
    while k:
        step += 1
        up, down = rotate_belt(up, down)
        move_robots(up, down)
        put_robot(up)

    print(step)


if __name__ == "__main__":
    main()
