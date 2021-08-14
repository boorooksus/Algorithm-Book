from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None

        index = inorder.index(preorder.pop(0))

        parent = TreeNode(inorder[index])
        parent.left = self.buildTree(preorder, inorder[:index])
        parent.right = self.buildTree(preorder, inorder[index + 1:])

        return parent


"""
1:preorder.index(inorder.index(parent.val) + 1)
"""