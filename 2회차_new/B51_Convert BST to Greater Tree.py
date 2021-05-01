# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        node = root
        cur = 0
        stack = []

        while node or stack:
            while node:
                stack.append(node)
                node = node.right

            node = stack.pop()
            node.val += cur
            cur = node.val

            node = node.left

        return root

