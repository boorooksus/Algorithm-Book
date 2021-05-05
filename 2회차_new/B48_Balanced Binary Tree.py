import sys

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        stack = [(root, 0)]
        min_dept = sys.maxsize
        max_dept = -sys.maxsize

        while stack:
            node, dept = stack.pop()

            if not node.left or not node.right:
                min_dept = min(min_dept, dept)
                max_dept = max(max_dept, dept)

            if node.left:
                stack.append((node.left, dept + 1))
            if node.right:
                stack.append((node.right, dept + 1))

        if max_dept - min_dept > 1:
            return False
        else:
            return True

