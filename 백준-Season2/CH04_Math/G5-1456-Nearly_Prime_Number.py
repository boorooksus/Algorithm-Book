from sys import stdin
from math import sqrt
input = lambda: stdin.readline().rstrip()

a, b = map(int, input().split())

MAX_INT = int(sqrt(b)) + 1

is_prime = [True] * MAX_INT
is_prime[1] = False
ans = 0

for i in range(2, MAX_INT):
    if is_prime[i]:
        for j in range(i * 2, MAX_INT, i):
            is_prime[j] = False

        nearly_prime = i * i
        while nearly_prime <= b:
            if a <= nearly_prime <= b:
                ans += 1
            nearly_prime *= i

print(ans)
