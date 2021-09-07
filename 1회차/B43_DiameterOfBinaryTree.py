from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    diameter = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        dq = deque([root])

        def dfs(cur):
            if cur is None:
                return 0

            left_len, right_len = 0, 0
            if cur.left is not None:
                left_len = dfs(cur.left)
            if cur.right is not None:
                right_len = dfs(cur.right)

            if left_len + right_len > self.diameter:
                self.diameter = left_len + right_len
            return 1 + max(left_len, right_len)

        dfs(root)
        return self.diameter


# leetcode: 543
# binary tree, dfs
