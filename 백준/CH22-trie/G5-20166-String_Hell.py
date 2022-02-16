from sys import stdin
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(list)


class Trie:
    def __init__(self):
        self.root = TrieNode()


def main():
    def input():
        return stdin.readline().rstrip()

    n, m, k = map(int, input().split())
    board = [list(input()) for _ in range(n)]


if __name__ == "__main__":
    main()
