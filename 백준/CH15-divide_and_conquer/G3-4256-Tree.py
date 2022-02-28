from sys import stdin
from typing import List, Optional


class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None


def build_tree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    if not inorder:
        return None
    root = TreeNode(preorder.pop(0))
    idx = inorder.index(root.val)
    root.left = build_tree(preorder, inorder[:idx])
    root.right = build_tree(preorder, inorder[idx + 1:])
    return root


def get_postorder(node: TreeNode) -> List[int]:
    if not node:
        return []
    postorder = []
    postorder.extend(get_postorder(node.left))
    postorder.extend(get_postorder(node.right))
    postorder.append(node.val)

    return postorder


def main():
    def input():
        return stdin.readline().rstrip()

    t = int(input())
    for _ in range(t):
        n = int(input())
        preorder = list(map(int, input().split()))
        inorder = list(map(int, input().split()))

        root = build_tree(preorder, inorder)
        postorder = get_postorder(root)
        print(*postorder)


if __name__ == "__main__":
    main()
