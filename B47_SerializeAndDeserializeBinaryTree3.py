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
        result = ['#']
        dq = deque([root])
        while dq:
            node = dq.popleft()
            if node:
                result.append(str(node.val))
                dq.append(node.left)
                dq.append(node.right)
            else:
                result.append('#')
        return ' '.join(result)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "# #":
            return None

        nodes = data.split()
        idx = 2
        result = TreeNode(int(nodes[1]))
        dq = deque([result])
        while dq:
            node = dq.popleft()
            if nodes[idx] != "#":
                node.left = TreeNode(int(nodes[idx]))
                dq.append(node.left)
            idx += 1

            if nodes[idx] != "#":
                node.right = TreeNode(int(nodes[idx]))
                dq.append(node.right)
            idx += 1
        return result


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

"""
leetcode: 297

"""