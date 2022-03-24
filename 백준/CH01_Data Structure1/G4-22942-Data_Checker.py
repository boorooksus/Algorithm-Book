from sys import stdin
from collections import deque


def main():
    def input():
        return stdin.readline().rstrip()

    n = int(input())
    circles = []
    for i in range(n):
        x, r = map(int, input().split())
        circles.append((x - r, i, 0))
        circles.append((x + r, i, 1))

    circles.sort()
    stack = []
    crds = set()
    for crd, i, flag in circles:
        if crd in crds:
            print("NO")
            return
        if flag == 0:
            stack.append((crd, i))
        elif stack[-1][1] != i:
            print("NO")
            return
        else:
            crds.add(crd)
            stack.pop()
    print("YES")


if __name__ == "__main__":
    main()
