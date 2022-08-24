from sys import stdin
from typing import List
input = lambda: stdin.readline().rstrip()


def query(start: int, end: int, inc: int) -> List[int]:
    stack, counter = [], [0] * (N + 1)
    for i in range(start, end, inc):
        while stack and heights[stack[-1]] <= heights[i]:
            stack.pop()
        if stack:
            counter[i] += counter[stack[-1]] + 1
            if not nearest[i] or i - nearest[i] > stack[-1] - i:
                nearest[i] = stack[-1]
        stack.append(i)
    return counter


if __name__ == "__main__":
    N = int(input())
    heights = [0] + list(map(int, input().split()))

    nearest = [''] * (N + 1)
    left = query(1, N + 1, 1)
    right = query(N, 0, -1)

    for i in range(1, N + 1):
        print(left[i] + right[i], nearest[i])
