from sys import stdin
from math import factorial


N = int(stdin.readline())

num = factorial(N)
for i in str(num)[::-1]:
    if i != '0':
        print(i)
        break


# res = 1
# for i in range(N, 1, -1):
#     res *= i
#     while res % 10 == 0:
#         res //= 10
#     # res %= 10000
#
# print(res % 10)


