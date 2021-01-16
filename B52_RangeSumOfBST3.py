from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if not root:
            return 0

        res = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node and node.val < low:
                stack.append(node.right)
            elif node and node.val > high:
                stack.append(node.left)
            elif node:
                res += node.val
                stack.append(node.left)
                stack.append(node.right)
        return res


"""
leetcode: 938
DFS 이용한 풀이2 (재귀 대신 반복 이용)
"""