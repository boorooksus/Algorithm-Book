from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    ans = 0
    def longestUnivaluePath(self, root: TreeNode) -> int:
        def dfs(cur: TreeNode) -> int:
            if cur is None:
                return 0

            left = dfs(cur.left)
            right = dfs(cur.right)

            if cur.left and cur.left.val == cur.val:
                left += 1
            else:
                left = 0
            if cur.right and cur.right.val == cur.val:
                right += 1
            else:
                right = 0

            self.ans = max(self.ans, left + right)
            return max(left, right)

        dfs(root)
        return self.ans










# leetcode: 687

