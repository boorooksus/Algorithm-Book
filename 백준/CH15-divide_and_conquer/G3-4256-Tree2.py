"""
코드 최적화
"""

from sys import stdin
from typing import List


def get_postorder(preorder: List[int], inorder: List[int]):
    if not inorder:
        return
    node = preorder.pop(0)
    idx = inorder.index(node)
    get_postorder(preorder, inorder[:idx])
    get_postorder(preorder, inorder[idx + 1:])
    print(node, end=' ')


def main():
    def input():
        return stdin.readline().rstrip()

    t = int(input())
    for _ in range(t):
        n = int(input())
        preorder = list(map(int, input().split()))
        inorder = list(map(int, input().split()))

        get_postorder(preorder, inorder)
        print()


if __name__ == "__main__":
    main()
