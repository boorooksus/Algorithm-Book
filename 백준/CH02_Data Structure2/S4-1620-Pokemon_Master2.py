"""
트라이 풀이
메모리 초과
"""
from sys import stdin
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.num = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num: int, pokemon: str) -> None:
        node = self.root
        for char in pokemon:
            node = node.children[char]
        node.num = num

    def find(self, pokemon: str) -> int:
        node = self.root
        for char in pokemon:
            node = node.children[char]
        return node.num


def main():
    def input():
        return stdin.readline().rstrip()

    n, m = map(int, input().split())
    trie = Trie()
    by_num = {}
    for i in range(1, n + 1):
        pokemon = input()
        trie.insert(i, pokemon)
        by_num[i] = pokemon

    for _ in range(m):
        x = input()
        if x.isdigit():
            print(by_num[int(x)])
        else:
            print(trie.find(x))


if __name__ == "__main__":
    main()
