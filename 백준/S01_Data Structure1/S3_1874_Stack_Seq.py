from sys import stdin
from collections import deque

n = int(stdin.readline())
seq = deque([])
for _ in range(n):
    seq.append(int(stdin.readline()))

stack, result = [], []
for i in range(1, n + 1):
    stack.append(i)
    result.append('+')

    while seq and stack and stack[-1] == seq[0]:
        stack.pop()
        seq.popleft()
        result.append('-')

if seq:
    print('NO')
else:
    print('\n'.join(result))
