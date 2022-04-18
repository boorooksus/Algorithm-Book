"""
틀림
"""
from sys import stdin
from typing import List
from functools import cmp_to_key


order = ""
for i in range(26):
    order += chr(i + 65) + chr(i + 97)


def compare(a: List[str], b: List[str]) -> int:
    i = 0
    while i < len(a) and i < len(b):
        if a[i] != b[i]:
            if a[i].isdigit() and b[i].isdigit():
                if int(a[i]) == int(b[i]):
                    if a[i] < b[i]:
                        return 1
                    else:
                        return -1
                elif int(a[i]) > int(b[i]):
                    return 1
                else:
                    return -1
            elif a[i].isdigit() and not b[i].isdigit():
                return -1
            elif not a[i].isdigit() and b[i].isdigit():
                return 1
            else:
                if order.index(a[i]) > order.index(b[i]):
                    return 1
                else:
                    return -1
        i += 1

    if len(a) > i >= len(b):
        return 1
    elif len(b) > i >= len(a):
        return -1
    else:
        return 0


def natural_sort(words: List[str]) -> List[str]:
    seq = []
    for word in words:
        seq.append([])
        num = ""
        for char in word:
            if char.isdigit():
                num += char
                continue
            elif num:
                seq[-1].append(num)
                num = ""
            seq[-1].append(char)
        if num:
            seq[-1].append(num)

    seq.sort(key=cmp_to_key(compare))
    res = []
    for li in seq:
        res.append(''.join(li))
    return res


if __name__ == "__main__":
    def input():
        return stdin.readline().rstrip()

    N = int(input())
    words = [input() for _ in range(N)]

    print(*natural_sort(words), sep='\n')
