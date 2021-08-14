import sys
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if not root:
            return sys.maxsize

        left, right = root.left, root.right
        while left and left.right:
            left = left.right
        while right and right.left:
            right = right.left

        result = sys.maxsize
        if left:
            result = min(result, root.val - left.val)
        if right:
            result = min(result, right.val - root.val)

        return min(result, self.minDiffInBST(root.left), self.minDiffInBST(root.right))

