from typing import List
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.word_id = -1
        self.pal_ids = []


class Trie:
    @staticmethod
    def is_palindrome(word: str):
        return word == word[::-1]

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str, index: int) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for i, char in enumerate(reversed(word)):
            if self.is_palindrome(word[:len(word) - i]):
                node.pal_ids.append(index)
            node = node.children[char]

        node.word_id = index

    def search(self, word: str, index: int) -> List[List[int]]:
        """
        Returns if the word is in the trie.
        """
        result = []
        node = self.root

        # 탐색 도중 팰런드롬
        while word:
            if node.word_id != -1:
                if self.is_palindrome(word):
                    result.append([index, node.word_id])
            if word[0] not in node.children:
                return result
            node = node.children[word[0]]
            word = word[1:]

        # 탐색 종료 후
        if node.word_id != -1 and node.word_id != index:
            result.append([index, node.word_id])

        for pal_id in node.pal_ids:
            result.append([index, pal_id])

        return result



class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        answer = []
        trie = Trie()

        for i, word in enumerate(words):
            trie.insert(word, i)

        for i, word in enumerate(words):
            answer += trie.search(word, i)

        return answer
