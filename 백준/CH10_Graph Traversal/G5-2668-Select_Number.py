from sys import stdin
from collections import defaultdict
input = lambda: stdin.readline().rstrip()


def dfs(num: int) -> None:
    if not visit[num]:
        visit[num] = True
        for next in graph[num]:
            x.add(num)
            y.add(next)

            if x == y:
                ans.extend(list(y))
                return

            dfs(next)
        visit[num] = False


if __name__ == "__main__":
    N = int(input())
    graph = defaultdict(list)
    for i in range(1, N + 1):
        graph[i].append(int(input()))

    ans = []
    for i in range(1, N + 1):
        visit = [False] * (N + 1)
        x, y = set(), set()
        dfs(i)
    ans = set(ans)
    print(len(ans))
    print(*sorted(ans), sep='\n')
