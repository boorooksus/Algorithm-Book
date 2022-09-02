from sys import stdin

input = lambda: stdin.readline().rstrip()


def check(start: int, pattern: str) -> bool:
    if start + len(pattern) - 1 >= len(s):
        return False
    for i in range(len(pattern)):
        if s[start + i] != pattern[i]:
            return False
    return True


def dfs(idx: int) -> int:
    if idx >= len(s):
        return 0
    if dp[idx] != -1:
        return dp[idx]

    max_val = 0
    for j, pattern in enumerate(a):
        if check(idx, pattern):
            max_val = max(dfs(idx + len(pattern)) + x[j], max_val)
    max_val = max(dfs(idx + 1) + 1, max_val)

    dp[idx] = max_val
    return max_val


if __name__ == "__main__":
    s = input()
    m = int(input())
    a, x = [], []
    for _ in range(m):
        pattern, score = input().split()
        a.append(pattern)
        x.append(int(score))

    dp = [-1] * len(s)
    print(dfs(0))
