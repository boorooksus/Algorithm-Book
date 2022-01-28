from sys import stdin


n, k, q, m = 0, 0, 0, 0
sleep = []
checkers = []
check = []
scopes = []


def input():
    return stdin.readline().strip()


def main():
    global n, k, q, m, sleep, checkers, scopes, check

    n, k, q, m = map(int, input().split())
    check = [0] * (n + 3)
    sleepers = list(map(int, input().split()))
    checkers = list(map(int, input().split()))
    for _ in range(m):
        scopes.append(tuple(map(int, input().split())))

    for student in checkers:
        cur = student
        if cur in sleepers:
            continue

        while cur < len(check):
            if cur not in sleepers:
                check[cur] = 1
            cur += student

    for start, end in scopes:
        print(end - start + 1 - sum(check[start:end + 1]))


if __name__ == "__main__":
    main()
