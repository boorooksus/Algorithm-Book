# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    ans = 0
    def maxDepth(self, root: TreeNode) -> int:
        def bfs(root, cur):
            if root.left is None and root.right is None and cur > self.ans:
                self.ans = cur
                return

            if root.left:
                bfs(root.left, cur + 1)
            if root.right:
                bfs(root.right, cur + 1)

        if root is None:
            return 0

        bfs(root, 1)
        return self.ans


# LEETCODE: 104
# 이진트리, BFS
# WHILE 루프를 이용한 BFS로도 풀어볼 것

