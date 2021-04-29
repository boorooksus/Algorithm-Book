# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        nums = []

        def get_nums(root):
            nums.append(root.val)

            if root.left:
                get_nums(root.left)
            if root.right:
                get_nums(root.right)

        get_nums(root)

        nums.sort()
        res = 100000
        for i in range(1, len(nums)):
            res = min(res, abs(nums[i] - nums[i - 1]))
        return res


