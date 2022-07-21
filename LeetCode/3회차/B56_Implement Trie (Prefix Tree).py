class TrieNode:
    def __init__(self, end):
        self.children = {}
        self.end = end


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode(False)

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node, i = self.root, 0
        while node.children and i < len(word) and word[i] in node.children.keys():
            node = node.children[word[i]]
            i += 1

        while i < len(word):
            node.children[word[i]] = TrieNode(False)
            node = node.children[word[i]]
            i += 1
        node.end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for i in range(len(word)):
            if word[i] in node.children.keys():
                node = node.children[word[i]]
            else:
                return False
        return node.end

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for i in range(len(prefix)):
            if prefix[i] in node.children.keys():
                node = node.children[prefix[i]]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)