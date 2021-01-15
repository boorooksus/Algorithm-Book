from typing import List
from sys import setrecursionlimit

setrecursionlimit(10**9)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        node = TreeNode(nums[len(nums) // 2])
        node.left = self.sortedArrayToBST(nums[:(len(nums) // 2)])
        node.right = self.sortedArrayToBST(nums[(len(nums) // 2 + 1):])
        return node


"""
leetcode: 108
Balanced BST
"""