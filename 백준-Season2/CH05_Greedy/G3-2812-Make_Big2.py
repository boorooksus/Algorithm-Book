from sys import stdin
input = lambda: stdin.readline().rstrip()


if __name__ == "__main__":
    N, K = map(int, input().split())
    num = list(map(int, input()))

    stack = []
    for i in range(N):
        while K > 0 and stack and stack[-1] < num[i]:
            stack.pop()
            K -= 1
        stack.append(num[i])

    while K > 0:
        stack.pop()
        K -= 1

    print(''.join(map(str, stack)))


"""
스택 이용
"""