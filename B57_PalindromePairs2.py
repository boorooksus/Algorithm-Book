from typing import List
from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.word_id = -1
        self.pal_ids = []
        self.children = defaultdict(TrieNode)


class Trie:

    @staticmethod
    def is_pal(word: str):
        return word == word[::-1]

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, idx: int, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for i, char in enumerate(reversed(word)):
            if self.is_pal(word[:len(word) - i]):
                node.pal_ids.append(idx)
            node = node.children[char]
        node.word_id = idx

    def search(self, idx: int, word: str) -> List:
        """
        Returns if the word is in the trie.
        """
        res = []
        node = self.root

        # 트라이 탐색 중 나머지가 팰런드롬인 경우
        while word:
            if node.word_id >= 0:
                if self.is_pal(word):
                    res.append([idx, node.word_id])
            if word[0] not in node.children:
                return res
            node = node.children[word[0]]
            word = word[1:]

        # 단어 탐색이 끝난 후 팰런드롬인지 확인
        if node.word_id >= 0 and node.word_id != idx:
            res.append([idx, node.word_id])

        # 트라이 탐색 후 나머지가 팰런드롬인 경우
        for pal_id in node.pal_ids:
            res.append([idx, pal_id])

        return res





class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie = Trie()
        for i, word in enumerate(words):
            trie.insert(i, word)

        ans = []
        for i, word in enumerate(words):
            ans += trie.search(i, word)
        return ans


sol = Solution()
print(sol.palindromePairs(["abcd","dcba","lls","s","sssll"]))


"""
leetcode: 336
브루트포스 풀이. 시간 초과
"""