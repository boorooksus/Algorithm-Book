from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = 0
        dq = deque([root])

        while dq:
            node = dq.popleft()
            if low <= node.val <= high:
                res += node.val

            if low <= node.val and node.left:
                dq.append(node.left)

            if node.val <= high and node.right:
                dq.append(node.right)

        return res
