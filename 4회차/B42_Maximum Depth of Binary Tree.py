from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], dept: int) -> int:
            if node is None:
                return dept
            return max(dfs(node.left, dept + 1),
                       dfs(node.right, dept + 1))

        return dfs(root, 0) if root else 0
