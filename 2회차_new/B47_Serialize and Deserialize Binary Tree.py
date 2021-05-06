from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = ['#']
        dq = deque([root])
        while dq:
            node = dq.pop()

            if node:
                dq.appendleft(node.left)
                dq.appendleft(node.right)
                res.append(str(node.val))
            else:
                res.append('#')
        return ' '.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "# #":
            return None

        nodes = data.split()

        root = TreeNode(int(nodes[1]))
        dq = deque([root])
        idx = 2

        while dq:
            node = dq.pop()
            if nodes[idx] != "#":
                node.left = TreeNode(int(nodes[idx]))
                dq.appendleft(node.left)
            idx += 1

            if nodes[idx] != "#":
                node.right = TreeNode(int(nodes[idx]))
                dq.appendleft(node.right)
            idx += 1

        return root





# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
