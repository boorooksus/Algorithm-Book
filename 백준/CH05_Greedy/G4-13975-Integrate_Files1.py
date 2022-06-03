from sys import stdin
from typing import List


input = lambda: stdin.readline().rstrip()


def cal(arr: List[int]) -> int:
    if len(arr) == 1:
        return 0

    if len(arr) % 4 == 0:
        return sum(arr) * (len(arr) // 4 + 1)

    new_arr, res = [], 0
    while len(arr) > 1:
        temp = arr.pop(0)
        temp += arr.pop(0)
        new_arr.append(temp)
        res += temp

    if arr:
        new_arr.append(arr.pop())

    return res + cal(new_arr)


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        K = int(input())
        docs = list(map(int, input().split()))
        docs.sort()
        print(cal(docs))





"""
98 / 35 32 / 21 21 / 17 14 / 5 5 / 5 4 / 4 3 / 3 1 = 67 42 31 10 9 7 4 = 170
98 67 / 42 31 / 10 9 / 7 4 = 165 73 19 11 = 268
165 73 / 19 11 = 238 20 = 268
238 20 = 268

516 438  954

1 2 / 3 4 / 5 6 = 3 7 11 = 21
3 7 / 11 = 10
10 11 = 21



1 2 / 3 4 / 5 6 / 7 8 / 9 10
1 2 3 4 / 5 6 7 8 // 9 10
1 2 3 4 5 6 7 8 // 9 10
1 2 3 4 5 6 7 8  9 10

4 -> 2
6 -> 2 + a
8 -> 3
10 -> 
"""