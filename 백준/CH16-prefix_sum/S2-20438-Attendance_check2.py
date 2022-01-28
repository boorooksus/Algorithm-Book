from sys import stdin


def input():
    return stdin.readline().strip()


def main():
    n, k, q, m = map(int, input().split())
    sleep = [0] * (n + 3)
    check = [0] * (n + 3)
    for i in map(int, input().split()):
        sleep[i] = 1

    for i in map(int, input().split()):
        if sleep[i]:
            continue
        for j in range(i, len(check), i):
            if not sleep[j]:
                check[j] = 1

    prefix = [0]
    for i in range(1, len(check)):
        prefix.append(prefix[-1] + check[i])

    for _ in range(m):
        start, end = map(int, input().split())
        print(end - start + 1 - (prefix[end] - prefix[start - 1]))


if __name__ == "__main__":
    main()
