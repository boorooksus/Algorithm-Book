# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    ans = True

    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(cur: TreeNode):
            if cur is None:
                return 0

            left, right = dfs(cur.left), dfs(cur.right)
            if abs(left - right) > 1:
                self.ans = False

            return max(left, right) + 1

        dfs(root)
        return self.ans


"""
leetcode: 110
bfs
"""