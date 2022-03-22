"""
해석하기 쉽게 고침
union, find 함수를 기본으로 사용
"""
from sys import stdin


parents = []


def find(x: int) -> int:
    if x == parents[x]:
        return x
    parents[x] = find(parents[x])
    return parents[x]


# 패러미터를 받을 때, x < y 이도록 받기
def union(x: int, y: int) -> None:
    x, y = find(x), find(y)
    parents[y] = x


def main():
    def input():
        return stdin.readline().rstrip()
    global parents

    g = int(input())
    p = int(input())
    planes = [int(input()) for _ in range(p)]

    parents = list(i for i in range(g + 1))
    cnt = 0
    for plane in planes:
        plane = find(plane)
        # 도킹 가능한 게이트가 없는 경우
        if plane == 0:
            break
        union(plane - 1, plane)
        cnt += 1

    print(cnt)


if __name__ == "__main__":
    main()
