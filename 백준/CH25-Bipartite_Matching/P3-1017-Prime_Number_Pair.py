from sys import stdin


input = lambda: stdin.readline().rstrip()


def eratos() -> None:
    prime[1] = False
    for i in range(2, 50):
        if prime[i]:
            for j in range(i * 2, 2001, i):
                prime[j] = False


def dfs(start: int) -> int:
    if visit[start]:
        return 0
    visit[start] = True

    for node in graph[start]:
        if d[node] == 0 or dfs(d[node]):
            d[node] = start
            return 1
    return 0


if __name__ == "__main__":
    N = int(input())
    nums = list(map(int, input().split()))
    lefts, rights = [0], [0]
    prime = [True] * 2001
    eratos()

    for i in range(N):
        if nums[0] % 2 == nums[i] % 2:
            lefts.append(nums[i])
        else:
            rights.append(nums[i])

    graph = list([] for _ in range(len(lefts)))
    for i in range(1, len(lefts)):
        for j in range(1, len(rights)):
            if prime[lefts[i] + rights[j]]:
                graph[i].append(j)

    ans = []
    for i in graph[1]:
        d = [0] * len(rights)
        d[i] = 1
        cnt = 1
        for j in range(1, len(lefts)):
            visit = [False] * len(lefts)
            visit[1] = True
            cnt += dfs(j)
        if cnt == N // 2:
            ans.append(rights[i])

    if not ans:
        print(-1)
    else:
        ans.sort()
        print(*ans, sep=' ')
