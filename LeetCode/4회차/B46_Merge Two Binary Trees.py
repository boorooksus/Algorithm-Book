from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(a: Optional[TreeNode], b: Optional[TreeNode]) -> Optional[TreeNode]:
            if not a and not b:
                return None
            elif a and not b:
                a.left = dfs(a.left, None)
                a.right = dfs(a.right, None)
            elif not a and b:
                a, b = b, a
            else:
                a.val += b.val
                a.left = dfs(a.left, b.left)
                a.right = dfs(a.right, b.right)

            return a

        root1 = dfs(root1, root2)
        return root1


Solution().mergeTrees(None, TreeNode(1))
