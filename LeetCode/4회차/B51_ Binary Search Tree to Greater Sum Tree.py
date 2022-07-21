# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def dfs(node: TreeNode, total: int) -> int:
            if not node:
                return total
            right = dfs(node.right, total)
            node.val += right
            left = dfs(node.left, node.val)

            return left

        dfs(root, 0)
        return root

