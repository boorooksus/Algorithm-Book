# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        def dfs(node: TreeNode, sum_val):
            if node is None:
                return 0

            right = dfs(node.right, sum_val)

            node.val += right + sum_val

            left = dfs(node.left, node.val)

            return left + node.val - sum_val

        dfs(root, 0)
        return root

"""
leetcode: 538
"""