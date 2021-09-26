import sys
from collections import deque


n, k = map(int, sys.stdin.readline().split())

dq = deque([num for num in range(1, n + 1)])
result = []

while dq:
    dq.rotate(-k)
    result.append(dq.pop())

print('<' + ', '.join(map(str, result)) + '>')
