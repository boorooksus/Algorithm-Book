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
        prev = -sys.maxsize
        ans = sys.maxsize

        node = root
        stack = []

        while node or stack:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            ans = min(ans, node.val - prev)
            prev = node.val

            node = node.right

        return ans

