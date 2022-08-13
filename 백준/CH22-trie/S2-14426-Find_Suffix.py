from sys import stdin
from collections import defaultdict
input = lambda: stdin.readline().rstrip()


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.cnt = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.children[char]
            node.cnt += 1

    def check(self, suffix: str) -> bool:
        node = self.root
        for char in suffix:
            node = node.children[char]
            if node.cnt == 0:
                return False
        return True


if __name__ == "__main__":
    N, M = map(int, input().split())
    trie = Trie()
    ans = 0
    for _ in range(N):
        trie.insert(input())
    for _ in range(M):
        ans += 1 if trie.check(input()) else 0

    print(ans)
