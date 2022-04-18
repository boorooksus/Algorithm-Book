"""
틀림
"""
from sys import stdin
from typing import List
from functools import cmp_to_key


# order: AaBbCc...XxYyZz
order = ""
for i in range(26):
    order += chr(i + 65) + chr(i + 97)


# 문자열 리스트 변환 함수
def str2li(word: str) -> List[str]:
    li = []
    num = ""
    for char in word:
        if char.isdigit():
            num += char
            continue
        elif num:
            li.append(num)
            num = ""
        li.append(char)
    if num:
        li.append(num)
    return li


def compare(x: str, y: str) -> int:
    a, b = str2li(x), str2li(y)
    i = 0
    while i < len(a) and i < len(b):
        if a[i] != b[i]:
            # 둘 다 숫자
            if a[i].isdigit() and b[i].isdigit():
                # 같은 값을 가지는 경우
                if int(a[i]) == int(b[i]):
                    if a[i] < b[i]:
                        return 1
                    else:
                        return -1
                elif int(a[i]) > int(b[i]):
                    return 1
                else:
                    return -1
            # a는 숫자, b는 문자
            elif a[i].isdigit() and not b[i].isdigit():
                return -1
            # a는 문자, b는 숫자
            elif not a[i].isdigit() and b[i].isdigit():
                return 1
            # 둘 다 문자
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


if __name__ == "__main__":
    def input():
        return stdin.readline().rstrip()

    N = int(input())
    words = [input() for _ in range(N)]

    words.sort(key=cmp_to_key(compare))
    print(*words, sep='\n')
