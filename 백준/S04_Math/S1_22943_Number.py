from sys import stdin
from itertools import combinations, combinations_with_replacement


k, m = map(int, stdin.readline().split())

# make numbers using 0-9
comb = list(combinations([str(i) for i in range(10)], k))
nums = set(int(''.join(i)) for i in comb if i[0] != '0')

# get prime numbers
primes = [i for i in range(2, m)]
for prime in primes:
    i = 2
    while prime * i < m:
        if prime * i in primes:
            primes.remove(prime * i)
        i += 1

# get numbers satisfying rule1, rule2
rule1 = list(combinations(primes, 2))
rule1 = set(i[0] + i[1] for i in rule1)
rule2 = list(combinations_with_replacement(primes, 2))
rule2 = list(i[0] * i[1] for i in rule2)
for i in range(len(rule2)):
    while rule2[i] % m == 0:
        rule2[i] //= m
rule2 = set(rule2)

# get numbers satisfying all conditions
result = nums.intersection(rule1)
result = result.intersection(rule2)

print(len(result))

"""
시간 초과
"""
