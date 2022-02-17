from sys import stdin


n = int(stdin.readline())
nums = set(list(map(int, stdin.readline().split())))

is_prime = [False, False] + [True] * (1000000 - 1)
for i in range(2, len(is_prime)):
    if not is_prime[i]:
        continue
    for j in range(2 * i, len(is_prime), i):
        is_prime[j] = False

res = 1
for num in nums:
    if is_prime[num]:
        res *= num

if res == 1:
    res *= -1
print(res)
