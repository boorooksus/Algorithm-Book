from sys import stdin


a, b = map(int, stdin.readline().split())

cnt, limit = 0, int(b ** 0.5) + 1
primes = [True] * ((10 ** 7) + 2)
for i in range(2, limit):
    if not primes[i]:
        continue
    j = i ** 2
    while j <= b:
        if j >= a:
            cnt += 1
        j *= i
    j = 2
    while i * j <= limit:
        primes[i * j] = False
        j += 1
print(cnt)
