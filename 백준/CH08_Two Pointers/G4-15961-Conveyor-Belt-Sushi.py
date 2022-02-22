from sys import stdin
from collections import defaultdict, deque


def main():
    def input():
        return stdin.readline()

    N, d, k, c = map(int, input().split())
    sushis = [int(input()) for _ in range(N)]

    window = deque()
    cnts = defaultdict(int)

    for i in range(k):
        window.append(sushis[i])
        cnts[sushis[i]] += 1

    res = 0
    cnt = len(cnts)
    if not cnts[c]:
        res = cnt + 1

    for start in range(N - 1):
        prev = window.popleft()
        cnts[prev] -= 1
        if cnts[prev] == 0:
            cnt -= 1
        window.append(sushis[(start + k) % N])
        cnts[window[-1]] += 1
        if cnts[window[-1]] == 1:
            cnt += 1
        if cnts[c] == 0:
            res = max(cnt + 1, res)
        else:
            res = max(cnt, res)

    print(res)


if __name__ == "__main__":
    main()
