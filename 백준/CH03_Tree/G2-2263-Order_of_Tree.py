from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 9)
input = lambda: stdin.readline().rstrip()


def get_preorder(in_start, in_end, post_start, post_end) -> None:
    if in_start >= in_end or post_start >= post_end:
        return

    preorder.append(postorder[post_end - 1])
    root = indices[postorder[post_end - 1]]
    get_preorder(in_start, root, post_start, post_start + root - in_start)
    get_preorder(root + 1, in_end, post_start + root - in_start, post_end - 1)


if __name__ == "__main__":
    n = int(input())
    inorder = list(map(int, input().split()))
    postorder = list(map(int, input().split()))

    preorder = []
    indices = {inorder[i]: i for i in range(0, len(inorder))}
    get_preorder(0, len(inorder), 0, len(postorder))
    print(*preorder)

"""
         1
       2    3
     4  5  6  7
     
in: 4 2 5 [1] 6 3 7 -> 
post: 4 5 2 / 6 7 3 [1]

pre: [1] 2 4 5 3 6 

"""
