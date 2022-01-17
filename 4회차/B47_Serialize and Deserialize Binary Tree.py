from collections import deque


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = ['N']
        dq = deque([root])
        while dq:
            node = dq.popleft()
            if node:
                res.append(str(node.val))
                dq.append(node.left)
                dq.append(node.right)
            else:
                res.append('N')
        return ' '.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == 'N N':
            return None

        nodes = data.split()

        root = TreeNode(int(nodes[1]))
        dq = deque([root])
        cur = 2

        while dq:
            node = dq.popleft()
            if nodes[cur] != 'N':
                node.left = TreeNode(int(nodes[cur]))
                dq.append(node.left)
            cur += 1
            if nodes[cur] != 'N':
                node.right = TreeNode(int(nodes[cur]))
                dq.append(node.right)
            cur += 1

        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))