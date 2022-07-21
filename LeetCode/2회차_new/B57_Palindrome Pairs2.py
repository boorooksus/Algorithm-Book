from typing import List
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.word_id = -1
        self.palindrome_word_id = []
        self.children = defaultdict(TrieNode)


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    @staticmethod
    def is_palindrome(word: str) -> bool:
        return True if word == word[::-1] else False

    def insert(self, index: int, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for i, char in enumerate(reversed(word)):
            if self.is_palindrome(word[0:len(word) - i]):
                node.palindrome_word_id.append(index)
            node = node.children[char]
        node.word_id = index

    def search(self, index: int, word: str) -> List:
        """
        Returns if the word is in the trie.
        """
        res = []
        node = self.root
        while word:
            if node.word_id > -1 and self.is_palindrome(word):
                res += [index, node.word_id],
            if word[0] not in node.children:
                return res
            node = node.children[word[0]]
            word = word[1:]

        if -1 < node.word_id != index:
            res += [index, node.word_id],

        for p in node.palindrome_word_id:
            res += [index, p],
        return res


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        t = Trie()
        res = []

        for i, word in enumerate(words):
            t.insert(i, word)

        for i, word in enumerate(words):
            res.extend(t.search(i, word))
        return res


print(Solution().palindromePairs(["abcd","dcba","lls","s","sssll"]))