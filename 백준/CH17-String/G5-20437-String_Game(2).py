from sys import stdin
from collections import defaultdict


def string_game(w: str, k: int) -> None:
    cnts = defaultdict(list)

    res = [10001, 0]

    for i, char in enumerate(w):
        cnts[char].append(i)

        if len(cnts[char]) >= k:
            res[0] = min(i - cnts[char][-k] + 1, res[0])
            res[1] = max(i - cnts[char][-k] + 1, res[1])

    if not res[1]:
        print(-1)
    else:
        print(res[0], res[1], sep=' ')


def main():
    t = int(stdin.readline())
    for _ in range(t):
        w = stdin.readline().rstrip()
        k = int(stdin.readline())
        string_game(w, k)


if __name__ == "__main__":
    main()
