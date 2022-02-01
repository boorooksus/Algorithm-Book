import sys
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.cnt = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.total_cnt = 0

    def insert_word(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.children[char]
        node.cnt += 1
        self.total_cnt += 1

    def show_cnt(self) -> None:
        node = self.root
        self.dfs(node, '')

    def dfs(self, node: TrieNode, prefix: str) -> None:
        if node.cnt > 0:
            print("%s %.4f" % (prefix, (node.cnt / self.total_cnt * 100)))

        for char in sorted(node.children.keys()):
            self.dfs(node.children[char], prefix + char)


def main():
    trie = Trie()
    lines = sys.stdin.readlines()
    for line in lines:
        trie.insert_word(line.strip())

    trie.show_cnt()


if __name__ == "__main__":
    main()
