import sys
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    prev = -sys.maxsize
    ans = sys.maxsize

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        node = root
        stack = []

        while node or stack:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            self.ans = min(self.ans, node.val - self.prev)
            self.prev = node.val

            node = node.right

        return self.ans
    
