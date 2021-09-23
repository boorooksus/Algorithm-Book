from sys import stdin
from collections import defaultdict


class TreeNode():
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None


n = int(stdin.readline())
children = defaultdict(list)
for i in range(n):
    parent = int(stdin.readline())
    if parent != -1:
        children[parent].append(i)

