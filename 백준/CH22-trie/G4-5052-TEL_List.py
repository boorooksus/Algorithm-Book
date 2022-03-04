from sys import stdin
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.end = False
        self.cnt = 0
        self.children = defaultdict(TrieNode)


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.consistency = True

    def insert(self, tel: str) -> None:
        if not self.consistency:
            return

        node = self.root
        for char in tel:
            if not char.isdigit():
                continue

            node = node.children[char]
            node.cnt += 1

            if node.end:
                self.consistency = False
                return

        node.end = True
        if node.cnt > 1:
            self.consistency = False

    def check_consistency(self) -> bool:
        return self.consistency


def main():
    def input():
        return stdin.readline().rstrip()

    t = int(input())
    for _ in range(t):
        n = int(input())
        trie = Trie()
        for _ in range(n):
            tel = input()
            trie.insert(tel)
        print(['NO', 'YES'][trie.check_consistency()])


if __name__ == "__main__":
    main()
