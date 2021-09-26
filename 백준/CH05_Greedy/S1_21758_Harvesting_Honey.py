from sys import stdin


n = int(stdin.readline())
honey = list(map(int, stdin.readline().split()))


def harvest(x: int, y: int, hive: int) -> int:
    result = 0
    for i in range(len(honey)):
        if i == x or i == y:
            continue
        if x < hive and x < i <= hive \
                or hive < x and hive <= i < x:
            result += honey[i]
        if y < hive and y < i <= hive \
                or hive < y and hive <= i < y:
            result += honey[i]
    return result


result = 0
for hive in range(len(honey)):
    for i in range(0, len(honey) - 1):
        if i == hive:
            continue
        for j in range(i + 1, len(honey)):
            if j == hive:
                continue
            result = max(result, harvest(i, j, hive))

print(result)

"""
서브태스크 배점 11점
"""