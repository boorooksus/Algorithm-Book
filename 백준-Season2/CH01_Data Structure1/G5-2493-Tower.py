from sys import stdin
input = lambda: stdin.readline().rstrip()


if __name__ == "__main__":
    N = int(input())
    towers = list(map(int, input().split()))

    ans = [0] * N
    stack = []
    for i, h in enumerate(towers):
        while stack and stack[-1][1] < h:
            stack.pop()
        if stack:
            ans[i] = stack[-1][0] + 1
        stack.append((i, h))

    print(' '.join(map(str, ans)))
    