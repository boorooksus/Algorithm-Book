from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 9)
input = lambda: stdin.readline().rstrip()


def get_preorder(in_start: int, in_end: int, post_start: int, post_end: int) -> None:
    if in_start >= in_end or post_start >= post_end:
        return

    preorder.append(postorder[post_end - 1])
    root = indices[preorder[-1]]

    get_preorder(in_start, root, post_start, post_start + root - in_start)
    get_preorder(root + 1, in_end, post_start + root - in_start, post_end - 1)


if __name__ == "__main__":
    n = int(input())
    inorder = list(map(int, input().split()))
    postorder = list(map(int, input().split()))

    preorder = []
    indices = {inorder[i]: i for i in range(n)}
    get_preorder(0, n, 0, n)
    print(' '.join(map(str, preorder)))


"""
트리 순회 문제
함수 인자로 리스트가 아닌 인덱스를 전달하여 메모리를 줄여야함
get_preorder(inorder: List[int], postorder: List[int])
->
get_preorder(in_start: int, in_end: int, post_start: int, post_end: int)
"""
