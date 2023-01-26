from sys import stdin
from collections import deque
input = lambda: stdin.readline().rstrip()


def rotate_left(wheel: int, direction: int) -> None:
    if wheel == 0 or wheels[wheel][2] == wheels[wheel + 1][6]:
        return

    rotate_left(wheel - 1, -direction)
    wheels[wheel].rotate(direction)


def rotate_right(wheel: int, direction: int) -> None:
    if wheel == 5 or wheels[wheel - 1][2] == wheels[wheel][6]:
        return

    rotate_right(wheel + 1, -direction)
    wheels[wheel].rotate(direction)


def calculate_score() -> int:
    score = 0
    for i in range(1, 5):
        if wheels[i][0] == '1':
            score += 2 ** (i - 1)
    return score


if __name__ == "__main__":
    wheels = [deque()] + list(deque(input()) for _ in range(4))
    K = int(input())
    for _ in range(K):
        n, d = map(int, input().split())
        rotate_left(n - 1, -d)
        rotate_right(n + 1, -d)
        wheels[n].rotate(d)

    print(calculate_score())


"""
톱니바퀴 index
    0
6       2
    4
"""
