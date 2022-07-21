from collections import defaultdict


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tree = defaultdict(list)

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        # 'S': 단어 시작, 'E': 단어 끝, '#': 사용된 문자
        prev = 'S'
        for letter in word:
            self.tree['#'].append(letter)
            self.tree[prev].append(letter)
            prev = letter
        self.tree[word[-1]].append('E')

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = 'S'
        for i in word:
            if i not in self.tree[cur]:
                return False
            cur = i
        if 'E' in self.tree[word[-1]]:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = '#'
        for i in prefix:
            if i not in self.tree[cur]:
                return False
            cur = i
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


"""
leetcode: 208
틀림. 단어에 연속으로 중복된 letter가 있는 경우와 한 번만 있는 경우 구분 못함
ex) 'add'를 insert 했을 때 'ad' search -> expected: False, output: True
"""