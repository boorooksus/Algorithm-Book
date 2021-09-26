from sys import stdin


def harvest(n: int) -> int:
    if n == 3:
        return max(honey) * 2

    result = 0
    # case1: 벌집이 맨 왼쪽, 오른쪽 벌 맨 오른쪽
    # [hive, ... , bee(left), ... bee(right)]
    # left: 왼쪽 벌 위치
    for left in range(1, len(honey) - 1):
        temp = 0
        for i in range(0, len(honey) - 1):
            if i < left:
                temp += honey[i] * 2
            elif left < i:
                temp += honey[i]

        result = max(result, temp)

    # case2: 왼쪽 벌 맨 왼쪽, 벌집이 맨 오른쪽
    # [bee(left), ... , bee(right), ... , hive]
    # right: 오른쪽 벌 위치
    for right in range(1, len(honey) - 1):
        temp = 0
        for i in range(1, len(honey)):
            if i < right:
                temp += honey[i]
            elif right < i:
                temp += honey[i] * 2

        result = max(result, temp)

    return result


n = int(stdin.readline())
honey = list(map(int, stdin.readline().split()))

print(harvest(n))

"""
서브태스크 배점 55점
"""