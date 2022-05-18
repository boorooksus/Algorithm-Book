from sys import stdin

input = lambda: stdin.readline().rstrip()


def check(start, end):

    if end - start <= 1:
        return True

    mid = start + (end - start) // 2
    for i in range(mid - start):
        if paper[start + i] == paper[end - i - 1]:
            return False

    return check(start, mid) and check(mid + 1, end)


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        paper = list(map(int, input()))

        print(['NO', 'YES'][check(0, len(paper))])
