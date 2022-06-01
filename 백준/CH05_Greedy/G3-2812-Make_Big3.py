from sys import stdin


input = lambda: stdin.readline().rstrip()


if __name__ == "__main__":
    N, K = map(int, input().split())
    nums = list(input())

    stack = []
    for num in nums:
        while K and stack and stack[-1] < num:
            K -= 1
            stack.pop()
        stack.append(num)

    while K:
        stack.pop()
        K -= 1

    print(''.join(stack))
