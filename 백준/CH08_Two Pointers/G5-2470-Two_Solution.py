from sys import stdin, maxsize
from typing import List


def main():
    def input():
        return stdin.readline().rstrip()

    n = int(input())
    solutions = list(map(int, input().split()))
    print(*mix(n, solutions))


def mix(n: int, solutions: List[int]) -> List[int]:
    solutions.sort()
    left, right = 0, len(solutions) - 1
    val = maxsize
    res = [0, 0]
    while left < right:
        mixed = solutions[left] + solutions[right]

        if abs(mixed) < val:
            val = abs(mixed)
            res = [solutions[left], solutions[right]]

        if mixed < 0:
            left += 1
        elif mixed == 0:
            return res
        else:
            right -= 1

    return res


if __name__ == "__main__":
    main()
