from sys import maxsize

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        prev = -maxsize
        res = maxsize

        stack = []
        node = root

        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()

            res = min(res, node.val - prev)
            prev = node.val

            node = node.right

        return res


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