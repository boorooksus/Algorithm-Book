"""
Boyer-Moore 알고리즘
시간초과
"""
from sys import stdin
from typing import List


# character jump에 사용하기 위하여 p에서 각 문자 위치를 저장한 테이블 생성
# (Last-Occurrence Function)
def set_table(p: str) -> List[int]:
    table = [-1] * 26
    for i in range(len(p) - 1, -1, -1):
        if table[ord(p[i]) - 97] == -1:
            table[ord(p[i]) - 97] = i
    return table


def character_jump(s: str, p: str, s_idx: int, p_idx: int, table: List[int]) -> int:
    l = table[ord(s[s_idx]) - 97]
    if l >= 0:
        return s_idx + len(p) - min(p_idx, 1 + l)
    else:
        return s_idx + len(p)


def boyer_moore(s: str, p: str) -> bool:
    i, j = len(p) - 1, len(p) - 1
    table = set_table(p)

    while i < len(s):
        if s[i] == p[j]:
            if j == 0:
                # i 번째에서 String Match
                return True
            else:
                i -= 1
                j -= 1
        else:
            i = character_jump(s, p, i, j, table)
            j = len(p) - 1

    return False


def main():
    s = stdin.readline().rstrip()
    p = stdin.readline().rstrip()

    print([0, 1][boyer_moore(s, p)])


if __name__ == "__main__":
    main()
