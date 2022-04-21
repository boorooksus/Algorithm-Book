from sys import stdin
from collections import defaultdict
from typing import List


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, words: List[str]) -> None:
        node = self.root
        for word in words:
            node = node.children[word]

    def dfs(self, node: TrieNode, dept: int) -> None:
        for child in sorted(list(node.children.keys())):
            print("--" * dept + child)
            self.dfs(node.children[child], dept + 1)

    def search(self) -> None:
        node = self.root
        self.dfs(node, 0)


if __name__ == "__main__":
    def input():
        return stdin.readline().rstrip()

    N = int(input())
    trie = Trie()
    for _ in range(N):
        temp = list(input().split())
        trie.insert(temp[1:])
    trie.search()
