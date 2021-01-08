# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def dfs(cur: TreeNode):
            if cur is None:
                return

            dfs(cur.left)
            dfs(cur.right)

            temp: TreeNode = cur.left
            cur.left = cur.right
            cur.right = temp

        dfs(root)
        return root


# leetcode: 226
