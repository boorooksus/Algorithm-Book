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
        dq = deque([root])
        while dq:
            node = dq.popleft()
            if node:
                if node.val < low:
                    dq.append(node.right)
                elif node.val > high:
                    dq.append(node.left)
                else:
                    res += node.val
                    dq.append(node.left)
                    dq.append(node.right)
        return res


"""
leetcode: 938
BFS 이용한 풀이
"""