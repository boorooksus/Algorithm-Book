from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        def dfs(cur: TreeNode) -> int:
            if cur.left and cur.val == cur.left.val:
                return dfs(cur.left) + 1
            elif cur.right and cur.val == cur.right.val:
                return dfs(cur.right) + 1
            else:
                return 0

        if root is None:
            return 0

        ans = 0
        dq = deque([root])
        while dq:
            cur: TreeNode = dq.popleft()
            if cur.left:
                dq.append(cur.left)
            if cur.right:
                dq.append(cur.right)

            left, right = 0, 0
            if cur.left and cur.val == cur.left.val:
                left = dfs(cur.left) + 1
            if cur.right and cur.val == cur.right.val:
                right = dfs(cur.right) + 1
            ans = max(ans, left + right)
        return ans


# leetcode: 687
# 틀림, 이유는 모름(오답 테스트 케이스가 너무 김)
