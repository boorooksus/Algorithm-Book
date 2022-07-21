from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        result = 0

        if not root:
            return result

        if root.val < low:
            result += self.rangeSumBST(root.right, low, high)
        elif root.val > high:
            result += self.rangeSumBST(root.left, low, high)
        else:
            result += root.val
            result += self.rangeSumBST(root.right, low, high)
            result += self.rangeSumBST(root.left, low, high)

        return result
