from sys import stdin


def dfs(target: int) -> None:
    parents[target] = -2

    for i, parent in enumerate(parents):
        if target == parent:
            dfs(i)


n = int(stdin.readline())  # number of nodes
parents = list(map(int, stdin.readline().split()))
k = int(stdin.readline())

dfs(k)
result = 0
for i in range(n):
    if parents[i] != -2 and i not in parents:
        result += 1
print(result)

