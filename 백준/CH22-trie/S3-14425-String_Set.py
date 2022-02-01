import sys
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert_word(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.children[char]
        node.end = True

    def find_word(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children.keys():
                return False
            node = node.children[char]
        return node.end


def main():
    s, m = map(int, sys.stdin.readline().split())

    trie = Trie()

    for _ in range(s):
        trie.insert_word(sys.stdin.readline().strip())

    res = 0
    for _ in range(m):
        if trie.find_word(sys.stdin.readline().strip()):
            res += 1

    print(res)


if __name__ == "__main__":
    main()
