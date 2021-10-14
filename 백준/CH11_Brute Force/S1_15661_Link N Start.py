import sys
from sys import stdin


n = int(stdin.readline())
stats = []
for _ in range(n):
    stats.append(list(map(int, stdin.readline().split())))

result = sys.maxsize
am, bm = 1, 2 ** n - 2  # a팀, b팀 여부 비트 마스크
while am < 2 ** n - 1:
    a, b = 0, 0  # 팀 능력치
    for i in range(n):
        for j in range(n):
            if i == j:
                continue

            if am & (1 << i) and am & (1 << j):
                a += stats[i][j]

            if bm & (1 << i) and bm & (1 << j):
                b += stats[i][j]

    result = min(result, abs(a - b))

    am += 1
    bm -= 1

print(result)



