"""
시간초과
"""
from sys import stdin
from collections import defaultdict
import os


dy = [1, 1, 0, -1, -1, -1, 0, 1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]
table = {1: 0, 2: 0, 3: 1, 4: 1, 5: 2, 6: 3, 7: 5, 8: 11}
board = []
words = []


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.crds = []


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.score = 0
        self.cnt = 0
        self.max_word = ''

        for i in range(4):
            for j in range(4):
                self.root.children[board[i][j]].crds.append((i, j))

    def dfs(self, word, idx, node, visit):

        node = node.children[word[idx]]
        if not node.crds:
            return False

        if idx == len(word) - 1:
            return True

        for y, x in node.crds:
            visit[y][x] = True
            for i in range(8):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < 4 and 0 <= nx < 4 and not visit[ny][nx]:
                    node.children[board[ny][nx]].crds.append((ny, nx))
            if self.dfs(word, idx + 1, node, visit):
                return True
            node.children.clear()
            visit[y][x] = False

        return False

    def boggle(self):
        for word in words:
            visit = [[False] * 4 for _ in range(4)]

            if self.dfs(word, 0, self.root, visit):
                self.cnt += 1
                self.score += table[len(word)]
                if len(word) >= len(self.max_word):
                    if len(word) == len(self.max_word):
                        self.max_word = min(word, self.max_word)
                    else:
                        self.max_word = word

        return self.score, self.max_word, self.cnt


def main():
    def input():
        return stdin.readline().rstrip()
    global board, words

    lines = list(map(str, os.read(0, 100000000).decode('utf-8').split('\n')))
    w = int(lines[0])
    words = []
    for i in range(1, w + 1):
        words.append(lines[i])
    b = int(lines[w + 2])
    for i in range(b):
        board = []
        for j in range(w + 3 + 5 * i, w + 7 + 5 * i):
            board.append(lines[j])
        trie = Trie()
        print("%d %s %d " % (trie.boggle()))


    # w = int(input())
    # words = set([input() for _ in range(w)])
    # _ = input()
    #
    # b = int(input())
    # for i in range(b):
    #     board = [input() for _ in range(4)]
    #     trie = Trie()
    #     print("%d %s %d " % (trie.boggle()))
    #
    #     if i < b - 1:
    #         _ = input()


if __name__ == "__main__":
    main()
