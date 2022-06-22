from sys import stdin
from collections import Counter


if __name__ == "__main__":
    x = stdin.readline().rstrip()

    table = {'w': 1, 'o': 2, 'l': 3, 'f': 4}
    i = 0
    while i < len(x):
        counts = Counter()
        for idx in range(1, 5):
            while i < len(x) and table[x[i]] == idx:
                counts[x[i]] += 1
                i += 1

        vals = sorted(list(counts.values()))
        if len(vals) != 4 or vals[0] != vals[-1]:
            print(0)
            exit()

    print(1)
