"""
BFS
틀림
"""
from sys import stdin
from collections import defaultdict, deque

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

    def bfs(self, word):
        dq = deque([(self.root.children[word[0]], 0, [])])
        while dq:
            node, idx, route = dq.popleft()

            if not node.crds:
                continue

            if idx == len(word) - 1:
                return True

            if not node.children:
                for y, x in node.crds:
                    for i in range(8):
                        ny, nx = y + dy[i], x + dx[i]
                        if 0 <= ny < 4 and 0 <= nx < 4:
                            node.children[board[ny][nx]].crds.append((ny, nx))

            for y, x in node.crds:
                if (y, x) not in route:
                    dq.append((node.children[word[idx + 1]], idx + 1, route[:] + [(y, x)]))

        return False

    def boggle(self):
        for word in words:
            if self.bfs(word):
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

    w = int(input())
    words = [input() for _ in range(w)]
    _ = input()

    b = int(input())
    for i in range(b):
        board = [input() for _ in range(4)]
        trie = Trie()
        print("%d %s %d " % (trie.boggle()))

        if i < b - 1:
            _ = input()


if __name__ == "__main__":
    main()
