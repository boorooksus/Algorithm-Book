from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        elif len(preorder) == 1:
            return TreeNode(preorder[0])

        parent = TreeNode(preorder[0])
        pre_right = inorder.index(parent.val) + 1

        if pre_right <= len(preorder):
            parent.left = self.buildTree(preorder[1:pre_right], inorder[:inorder.index(parent.val)])

        if inorder.index(parent.val) + 1 < len(inorder):
            parent.right = self.buildTree(preorder[pre_right:], inorder[inorder.index(parent.val) + 1:])

        return parent


"""
1:preorder.index(inorder.index(parent.val) + 1)
"""