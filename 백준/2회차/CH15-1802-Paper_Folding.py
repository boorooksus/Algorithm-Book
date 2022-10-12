from sys import stdin

input = lambda: stdin.readline().rstrip()


def divide_and_conquer(x: str, start: int, end: int) -> bool:
    if start == end - 1:
        return True

    mid = (start + end) // 2
    left, right = mid - 1, mid + 1
    while left >= start and right < end:
        if x[left] == x[right]:
            return False
        left -= 1
        right += 1

    return divide_and_conquer(x, start, mid) \
        and divide_and_conquer(x, mid + 1, end)


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        paper = input()
        print(['NO', 'YES'][divide_and_conquer(paper, 0, len(paper))])
