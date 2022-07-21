from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        postorder = deque()
        stack = []
        node = root

        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            postorder.append(node)

            node = node.right

        cur = 0
        while postorder:
            node = postorder.pop()
            cur += node.val
            node.val = cur

        return root

"""
중위순회 거꾸로
"""