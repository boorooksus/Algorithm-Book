from sys import stdin
from collections import defaultdict


class TrieNode:
    def __init__(self, y=-1, x=-1):
        self.children = defaultdict(list)
        self.y = y
        self.x = x


class Trie:
    def __init__(self, board, n, m):
        self.root = TrieNode()
        self.board = board
        self.n = n
        self.m = m
        self.dy = [1, 1, 0, -1, -1, -1, 0, 1]
        self.dx = [0, 1, 1, 1, 0, -1, -1, -1]

        for i in range(n):
            for j in range(m):
                self.root.children[self.board[i][j]].append(TrieNode(i, j))

    def find(self, node, word, idx) -> int:
        if idx == len(word):
            return 1

        res = 0

        if not node.children.keys():
            for i in range(len(self.dy)):
                ny = (node.y + self.dy[i]) % self.n
                nx = (node.x + self.dx[i]) % self.m
                node.children[self.board[ny][nx]].append(TrieNode(ny, nx))

        for child in node.children[word[idx]]:
            res += self.find(child, word, idx + 1)

        return res


def main():
    def input():
        return stdin.readline().rstrip()

    n, m, k = map(int, input().split())
    board = [list(input()) for _ in range(n)]
    trie = Trie(board, n, m)

    for _ in range(k):
        x = input()
        print(trie.find(trie.root, x, 0))


if __name__ == "__main__":
    main()
