from sys import stdin
from collections import defaultdict
from typing import List
input = lambda: stdin.readline().rstrip()


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.cnt = 0


class Trie:
    def __init__(self, arr: List[List[str]], n: int, m: int):
        self.root = TrieNode()
        self.arr = arr
        self.n = n
        self.m = m

    def dfs(self, y: int, x: int, cur: int, node: TrieNode) -> None:
        node.cnt += 1

        if cur == 5:
            return

        dy = [-1, -1, 0, 1, 1, 1, 0, -1]
        dx = [0, 1, 1, 1, 0, -1, -1, -1]

        for i in range(8):
            ny, nx = (y + dy[i]) % self.n, (x + dx[i]) % self.m
            self.dfs(ny, nx, cur + 1, node.children[self.arr[ny][nx]])

    def search(self) -> None:
        node = self.root

        for i in range(self.n):
            for j in range(self.m):
                self.dfs(i, j, 1, node.children[self.arr[i][j]])

    def count(self, word: str) -> int:
        node = self.root
        for char in word:
            node = node.children[char]
        return node.cnt


if __name__ == "__main__":
    N, M, K = map(int, input().split())
    trie = Trie([list(input()) for _ in range(N)], N, M)

    trie.search()

    for _ in range(K):
        print(trie.count(input()))
