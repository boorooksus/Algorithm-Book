"""
메모리 초과
"""
from sys import stdin
from collections import defaultdict


dy = [1, 1, 0, -1, -1, -1, 0, 1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]
board = []


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.crds = []


class Trie:
    def __init__(self, words):
        self.root = TrieNode()
        self.visit = [[False] * 4 for _ in range(4)]
        self.score = 0
        self.cnt = 0
        self.max_word = ''
        self.words = words
        self.table = {1: 0, 2: 0, 3: 1, 4: 1, 5: 2, 6: 3, 7: 5, 8: 11}

        for i in range(4):
            for j in range(4):
                self.root.children[board[i][j]].crds.append((i, j))

    def dfs(self, word, idx, node, visit):
        if len(word) == idx:
            return True

        node = node.children[word[idx]]
        if not node.crds:
            return False

        for y, x in node.crds:
            visit[y][x] = True
            for i in range(8):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < 4 and 0 <= nx < 4 and not visit[ny][nx]:
                    node.children[board[ny][nx]].crds.append((ny, nx))
            if self.dfs(word, idx + 1, node, visit):
                return True
            visit[y][x] = False

    def boggle(self):
        for word in self.words:
            node = self.root
            visit = [[False] * 4 for _ in range(4)]

            if self.dfs(word, 0, node, visit):
                self.cnt += 1
                self.score += self.table[len(word)]
                if len(word) >= len(self.max_word):
                    if len(word) == len(self.max_word):
                        self.max_word = min(word, self.max_word)
                    else:
                        self.max_word = word


def main():
    def input():
        return stdin.readline().rstrip()
    global board

    w = int(input())
    words = set([input() for _ in range(w)])
    _ = input()

    b = int(input())
    for i in range(b):
        board = [input() for _ in range(4)]
        trie = Trie(words)
        trie.boggle()
        print("%d %s %d " % (trie.score, trie.max_word, trie.cnt))

        if i < b - 1:
            _ = input()


if __name__ == "__main__":
    main()
