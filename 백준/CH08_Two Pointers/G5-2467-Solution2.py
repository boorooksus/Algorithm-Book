from sys import stdin
input = lambda: stdin.readline().rstrip()


INF = int(3e9)


if __name__ == "__main__":
    N = int(input())
    solutions = list(map(int, input().split()))

    solutions.sort()
    left, right = 0, N - 1
    min_val, indices = INF, [left, right]
    while left < right:
        mixed = solutions[left] + solutions[right]

        if abs(mixed) < min_val:
            min_val = abs(mixed)
            indices = [left, right]

        if mixed < 0:
            left += 1
        else:
            right -= 1

    print(solutions[indices[0]], solutions[indices[1]])
