from sys import stdin
from collections import defaultdict


input = lambda: stdin.readline().rstrip()


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, x: str) -> None:
        li = x.split('\\')
        node = self.root
        for name in li:
            node = node.children[name]

    def dfs(self, node: TrieNode, dept: int) -> None:
        for child in sorted(list(node.children.keys())):
            print(' ' * dept + child)
            self.dfs(node.children[child], dept + 1)

    def show(self) -> None:
        for child in sorted(list(self.root.children.keys())):
            print(child)
            self.dfs(self.root.children[child], 1)


if __name__ == "__main__":
    N = int(input())
    trie = Trie()
    for _ in range(N):
        d = input()
        trie.insert(d)
    trie.show()
