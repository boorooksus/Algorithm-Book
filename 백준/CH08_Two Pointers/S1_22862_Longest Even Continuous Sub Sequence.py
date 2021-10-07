from sys import stdin


n, k = map(int, stdin.readline().split())
seq = list(map(int, stdin.readline().split()))

left, right = 0, 0
removed = 0
result = 0

while right < n:
    if seq[right] % 2 == 1:
        if removed < k:
            removed += 1
        else:
            while left >= 0 and seq[left] % 2 == 0:
                left += 1
            left += 1
    result = max(result, right - left + 1 - removed)
    right += 1

print(result)
