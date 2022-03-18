"""
틀림
"""
from sys import stdin
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.route = False


class Trie:
    def __init__(self, words, board):
        self.root = TrieNode()
        self.dy = [1, 1, 0, -1, -1, -1, 0, 1]
        self.dx = [0, 1, 1, 1, 0, -1, -1, -1]
        self.visit = [[False] * 4 for _ in range(4)]
        self.board = board
        self.score = 0
        self.cnt = 0
        self.max_word = ''
        self.words = words
        self.table = {1: 0, 2: 0, 3: 1, 4: 1, 5: 2, 6: 3, 7: 5, 8: 11}

        for i in range(4):
            for j in range(4):
                self.visit[i][j] = True
                self.insert(i, j, self.root, 0)
                self.visit[i][j] = False

    def insert(self, y: int, x: int, node: TrieNode, cur: int):
        node.route = True

        if cur > 8:
            return

        for i in range(8):
            ny, nx = y + self.dy[i], x + self.dx[i]
            if 0 <= ny < 4 and 0 <= nx < 4 and not self.visit[ny][nx]:
                self.visit[ny][nx] = True
                self.insert(ny, nx, node.children[self.board[ny][nx]], cur + 1)
                self.visit[ny][nx] = False

    def boggle(self):
        for word in self.words:
            node = self.root
            for char in word:
                node = node.children[char]
                if not node.children[char].route:
                    break
            else:
                self.cnt += 1
                self.score += self.table[len(word)]
                if len(word) >= len(self.max_word):
                    if len(word) == len(self.max_word):
                        self.max_word = min(word, self.max_word)
                    else:
                        self.max_word = word

    def get_result(self):
        return self.score, self.max_word, self.cnt


def main():
    def input():
        return stdin.readline().rstrip()

    w = int(input())
    words = set([input() for _ in range(w)])
    _ = input()

    b = int(input())
    for i in range(b):
        board = [input() for _ in range(4)]
        trie = Trie(words, board)
        trie.boggle()
        print(*trie.get_result(), sep=' ')

        if i < b - 1:
            _ = input()


if __name__ == "__main__":
    main()




