"""
이분 매칭
이전 풀이에서 dfs의 visit 여부 체크를 아래 방식으로 변경
(직원의 visit 여부 -> 업무의 visit 여부)
참고: https://blog.naver.com/ndb796/221240613074
"""
from sys import stdin
from collections import defaultdict
from typing import List


input = lambda: stdin.readline().rstrip()


def dfs(start: int, visit: List[bool]) -> int:
    for node in graph[start]:
        if visit[node]:
            continue
        visit[node] = True
        if d[node] == 0 or dfs(d[node], visit):
            d[node] = start
            return 1
    return 0


if __name__ == "__main__":
    N, M, K = map(int, input().split())
    graph = defaultdict(list)
    d = [0] * (M + 1)

    for i in range(1, N + 1):
        query = list(map(int, input().split()))
        for j in range(1, len(query)):
            graph[i].append(query[j])

    ans = 0
    for i in range(1, N + 1):
        visit = [False] * (M + 1)
        ans += dfs(i, visit)

    for i in range(1, N + 1):
        while K > 0:
            visit = [False] * (M + 1)
            if dfs(i, visit):
                K -= 1
                ans += 1
            else:
                break
    print(ans)
