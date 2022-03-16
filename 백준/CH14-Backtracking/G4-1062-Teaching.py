"""
python 시간초과, pypy 통과

"""
from sys import stdin
from itertools import combinations


def main():
    def input():
        return stdin.readline().rstrip()

    n, k = map(int, input().split())
    words = [input()[4:-4] for _ in range(n)]

    learned = {'a', 'n', 't', 'i', 'c'}
    k -= len(learned)

    if k < 0:
        print(0)
        return

    elif k == 21:
        print(n)
        return

    letters = []
    for i in range(26):
        if chr(i + 97) not in learned:
            letters.append(chr(i + 97))

    res = 0
    combs = combinations(letters, k)
    for comb in combs:
        cnt = 0
        for word in words:
            for char in word:
                if char not in comb and char not in learned:
                    break
            else:
                cnt += 1
        res = max(cnt, res)

    print(res)


if __name__ == "__main__":
    main()
