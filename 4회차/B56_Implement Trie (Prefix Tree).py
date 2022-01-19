from collections import defaultdict


class TrieNode:
    def __init__(self, val: str):
        self.val = val
        self.next = {}
        self.end = 0


class Trie:

    def __init__(self):
        self.root = TrieNode(None)

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.next:
                node.next[char] = TrieNode(char)
            node = node.next[char]
        node.end = 1

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.next:
                return False
            node = node.next[char]
        return node.end == 1

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.next:
                return False
            node = node.next[char]
        return True


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert('apple')
param_2 = obj.search('apple')
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)