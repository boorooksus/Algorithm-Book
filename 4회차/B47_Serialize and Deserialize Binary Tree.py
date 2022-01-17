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
        res = ''
        dq = deque([root])
        while dq:
            node = dq.popleft()
            if node:
                res += str(node.val)
                dq.append(node.left)
                dq.append(node.right)
            else:
                res += 'N'
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data or data[0] == 'N':
            return None

        root = TreeNode(int(data[0]))
        dq = deque([root])
        cur = 1

        while dq:
            node = dq.popleft()
            if data[cur] != 'N':
                node.left = TreeNode(int(data[cur]))
                dq.appendleft(node.left)
            cur += 1
            if data[cur] != 'N':
                node.right = TreeNode(int(data[cur]))
                dq.appendleft(node.right)

        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))