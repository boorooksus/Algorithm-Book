from sys import stdin
input = lambda: stdin.readline().rstrip()


def check() -> bool:
    start, end = 0, n // 2 + 1
    while start <= end:
        mid = start + (end - start) // 2
        res = (n - mid + 1) * (mid + 1)
        if res > k:
            end = mid - 1
        elif res < k:
            start = mid + 1
        else:
            return True
    return False


if __name__ == "__main__":
    n, k = map(int, input().split())

    print(['NO', 'YES'][check()])




"""
   0 1 2 3 4 5
1: 2
2: 3 4
3: 4 4 6
4: 5 8 9 
5: 6 10 12

x + 1, (x - 1 + 1) * 2, (x - 2 + 1) * 3, ..., (x - l + 1) * (l + 1)
"""