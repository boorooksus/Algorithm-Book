from sys import stdin


input = lambda: stdin.readline().rstrip()


if __name__ == "__main__":
    N, M = (int(input()) for _ in range(2))
    parents = {i: i for i in range(1, N + 1)}
    intgs = sorted(list(list(map(int, input().split())) for _ in range(M)))
    for x, y in intgs:
        for i in range(x + 1, y + 1):
            parents[i] = parents[x]

    if M == 0:
        print(N)
        exit(0)

    print(len(set(parents.values())))
