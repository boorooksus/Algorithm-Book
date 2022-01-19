from typing import List
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.word_id = -1
        self.palindrome_ids = []


class Trie:
    def __init__(self):
        self.root = TrieNode()

    @staticmethod
    def is_pal(word: str) -> bool:
        return word[::] == word[::-1]

    def insert(self, word: str, index: int) -> None:
        node = self.root
        for i, char in enumerate(reversed(word)):
            if self.is_pal(word[:len(word) - i]):
                node.palindrome_ids.append(index)
            node = node.children[char]
        node.word_id = index

    def search(self, word: str, index: int) -> List[List[int]]:
        node = self.root
        res = []

        while word:
            # 탐색 중간에 word_id 있고, 나머지 문자가 팰런드롬
            if node.word_id != -1 and self.is_pal(word):
                res.append([index, node.word_id])
            if word[0] not in node.children:
                return res
            node = node.children[word[0]]
            word = word[1:]

        # 끝까지 탐색했을 때, word_id가 있는 경우
        if node.word_id != -1 and node.word_id != index:
            res.append([index, node.word_id])

        # 끝까지 탐색 했을 때, palindrome_word_ids가 있는 경우
        for palindrome_id in node.palindrome_ids:
            res.append([index, palindrome_id])

        return res


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie = Trie()
        for i, word in enumerate(words):
            trie.insert(word, i)

        res = []
        for i, word in enumerate(words):
            res.extend(trie.search(word, i))

        return res


Solution().palindromePairs(["abcd","dcba","lls","s","sssll"])
