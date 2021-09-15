from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 9)


class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None


def make_tree() -> TreeNode:
    val = int(stdin.readline())

    node = TreeNode(val)
    val.left = make_tree()
    val.right = make_tree()

    return node
