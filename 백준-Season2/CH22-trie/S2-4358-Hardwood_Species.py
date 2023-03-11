from sys import stdin
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.cnt = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.total = 0

    def insert(self, word: str) -> None:
        self.total += 1
        node = self.root
        for char in word:
            node = node.children[char]
        node.cnt += 1

    def get_species(self, node: TrieNode, route: str) -> None:
        if node.cnt > 0:
            print("%s %.4f" % (route, (node.cnt / self.total * 100)))

        for child in sorted(node.children.keys()):
            self.get_species(node.children[child], route + child)

    def print_result(self) -> None:
        self.get_species(self.root, "")


if __name__ == "__main__":
    trie = Trie()
    for line in stdin.readlines():
        trie.insert(line.strip())

    trie.print_result()


"""
트라이
문자열 출력 포맷
EOF 처리
"""
