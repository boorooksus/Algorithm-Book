from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        result = ""
        dq = deque([root])
        while dq:
            node = dq.popleft()
            result += str(node.val)
            if node.left:
                dq.append(node.left)
            if node.right:
                dq.append(node.right)
        return result

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        root = TreeNode(data[0])
        data = data[1:]
        dq = deque([root])
        while data:
            node = dq.popleft()
            node.left = TreeNode(int(data[0]))
            data = data[1:]
            dq.append(node.left)
            if data:
                node.right = TreeNode(int(data[0]))
                data = data[1:]
                dq.append(node.right)
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

"""
leetcode: 297
bfs로 풀이. 오류
"""