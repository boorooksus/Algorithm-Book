# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


MAX = 100000


class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        if not root:
            return MAX

        def get_min(node: TreeNode) -> int:
            if not node:
                return MAX
            return min(node.val, get_min(node.left))

        def get_max(node: TreeNode) -> int:
            if not node:
                return -1
            return max(node.val, get_max(node.right))

        left = get_max(root.left)
        if left == -1:
            left = MAX

        return min(abs(root.val - left),
                   abs(get_min(root.right) - root.val),
                   self.minDiffInBST(root.left),
                   self.minDiffInBST(root.right))


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