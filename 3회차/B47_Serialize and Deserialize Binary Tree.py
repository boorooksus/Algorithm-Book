from collections import deque


# Definition for a binary tree node.
# TreeNode 정의 지우고 채점해야 성공함

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        data = ""
        dq = deque([root])
        while dq:
            node = dq.popleft()

            if not node:
                data += "None "

            else:
                data += str(node.val) + " "
                dq.append(node.left)
                dq.append(node.right)
        return data

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        values = deque(data.split())
        cur = values.popleft()
        if cur == 'None':
            return None
        root = TreeNode(int(cur))
        nodes = deque([root])

        while len(values) > 1:
            node = nodes.popleft()
            cur = values.popleft()
            if cur != 'None':
                node.left = TreeNode(int(cur))
                nodes.append(node.left)
            cur = values.popleft()
            if cur != 'None':
                node.right = TreeNode(int(cur))
                nodes.append(node.right)
        return root


deser = Codec().deserialize("1 2 3 None None 4 5")
ser = Codec().serialize((deser))
print(ser)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
