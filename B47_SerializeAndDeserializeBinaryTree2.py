from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    result = ""
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def dfs(cur):
            if cur is None:
                return
            self.result += str(cur.val)
            dfs(cur.left)
            dfs(cur.right)

        return self.result

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data != "":
            node = TreeNode(int(data[0]))
            node.left = self.deserialize(data[1:len(data)//2])
            node.right = self.deserialize(data[len(data)//2 + 1:])
            return node
        else:
            return None


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

"""
leetcode: 297
dfs로 풀이
"""