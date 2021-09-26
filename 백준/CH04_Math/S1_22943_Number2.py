from sys import stdin


k, m = map(int, stdin.readline().split())

# get prime numbers
is_prime = [1 for _ in range(10 ** k)]
is_prime[0], is_prime[1] = 0, 0
for i in range(2, len(is_prime)):
    if is_prime[i] == 0:
        continue
    j = 2
    while i * j < len(is_prime):
        is_prime[i * j] = 0
        j += 1
primes = [i for i in range(2, 10 ** k) if is_prime[i] == 1]

# get numbers satisfying rule1 in prime number list
rule1 = set()
# use two pointer
left, right = 0, len(primes) - 1
for left in range(len(primes)):
    for right in range(len(primes) - 1, left, -1):
        temp = str(primes[left] + primes[right])
        if len(temp) > k:
            continue
        if len(temp) < k:
            break
        if len(set(temp)) == k:
            rule1.add(int(temp))

# get numbers satisfying rule2 in rule1 list
result = set()
for i in range(len(primes)):
    for j in range(i, len(primes)):
        temp = primes[i] * primes[j]
        if temp % m == 0:
            continue
        while temp < 10 ** k:
            if temp >= 10 ** (k - 1) and temp in rule1:
                result.add(temp)
            temp *= m

print(len(result))
