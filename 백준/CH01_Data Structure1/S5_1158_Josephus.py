import sys

n, k = map(int, sys.stdin.readline().split())

order = []
nums = list(num for num in range(1, n + 1))
num = -1
while nums:
    num = (num + k) % len(nums)
    order.append(nums.pop(num))
    num -= 1

print('<', end='')
for i in range(len(order) - 1):
    print(order[i], end=', ')
print(str(order[-1]) + '>')
