from sys import stdin
from itertools import permutations
from typing import List


def anagram(x: str) -> List[str]:
    res = set()
    for word in permutations(x):
        res.add(''.join(word))

    return sorted(list(res))


def main():
    def input():
        return stdin.readline().rstrip()

    n = int(input())
    for _ in range(n):
        res = anagram(input())
        for word in res:
            print(word)


if __name__ == "__main__":
    main()
