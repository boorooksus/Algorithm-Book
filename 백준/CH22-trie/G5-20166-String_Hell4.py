from sys import stdin
from collections import defaultdict


class TrieNode:
    def __init__(self,):
        self.children = defaultdict(TrieNode)
        self.cnt = 0


class Trie:
    def __init__(self, board, n, m):
        self.root = TrieNode()
        self.board = board
        self.n = n
        self.m = m

    def dfs(self, node, y: int, x: int, cur):
        dy = [1, 1, 0, -1, -1, -1, 0, 1]
        dx = [0, 1, 1, 1, 0, -1, -1, -1]

        # 문자열의 길이는 최대 5이므로 종료
        if cur == 5:
            return

        node = node.children[board[y][x]]
        node.cnt += 1

        for i in range(8):
            ny = (y + dy[i]) % n
            nx = (x + dx[i]) % m
            self.dfs(node, ny, nx, cur + 1)

    # 보드에서 생성 가능한 모든 5글자 문자열을 트라이에 입력
    def insert(self):
        node = self.root

        for i in range(self.n):
            for j in range(self.m):
                self.dfs(node, i, j, 0)

    def find(self, word) -> int:
        node = self.root
        for char in word:
            node = node.children[char]
        return node.cnt


def main():
    def input():
        return stdin.readline().rstrip()
    global n, m, board, trie

    n, m, k = map(int, input().split())
    board = [list(input()) for _ in range(n)]
    trie = Trie(board, n, m)
    trie.insert()

    words = [input() for _ in range(k)]

    for word in words:
        print(trie.find(word))


if __name__ == "__main__":
    main()
