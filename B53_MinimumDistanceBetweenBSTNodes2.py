from sys import maxsize

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    prev = -maxsize
    res = maxsize

    def minDiffInBST(self, root: TreeNode) -> int:
        if root.left:
            self.minDiffInBST(root.left)

        self.res = min(root.val - self.prev, self.res)
        self.prev = root.val

        if root.right:
            self.minDiffInBST(root.right)

        return self.res



root = cur = TreeNode(99)
cur.left = TreeNode(84)
cur = cur.left
cur.left = TreeNode(27)
cur = cur.left
cur.left = TreeNode(1)
cur.right = TreeNode(53)

sol = Solution()
print(sol.minDiffInBST(root))

"""
leetcode: 783
"""