from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        def dfs(a, b):
            a.val += b.val

            if a.left and b.left:
                dfs(a.left, b.left)
            if a.right and b.right:
                dfs(a.right, b.right)

            if a.left is None and b.left:
                a.left = b.left
                return
            elif a.right is None and b.right:
                a.right = b.right
                return
            else:
                return

        if t1 and t2:
            dfs(t1, t2)
        elif t1 is None and t2:
            t1 = t2
        return t1


# leetcode: 617
# 틀림. 이유는 모름(오답 테스트케이스가 너무 김)
