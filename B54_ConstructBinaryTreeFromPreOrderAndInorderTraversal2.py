from typing import List
from sys import setrecursionlimit
setrecursionlimit(10 ** 9)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not inorder:
            return None

        idx = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[idx])

        root.left = self.buildTree(preorder, inorder[:idx])
        root.right = self.buildTree(preorder, inorder[idx + 1:])
        return root


sol = Solution()
print(sol.buildTree([3,9,20,15,7], [9,3,15,20,7]))

"""
leetcode: 105
"""