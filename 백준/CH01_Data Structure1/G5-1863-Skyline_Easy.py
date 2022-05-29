from sys import stdin


input = lambda: stdin.readline().rstrip()


if __name__ == "__main__":
    n = int(input())
    buildings = list(list(map(int, input().split())) for _ in range(n))

    cnt = 0
    stack = []
    for x, y in buildings:
        while stack and stack[-1][1] > y:
            cnt += 1
            stack.pop()

        while stack and stack[-1][1] == y:
            stack.pop()

        if y > 0:
            stack.append([x, y])

    cnt += len(stack)
    print(cnt)
