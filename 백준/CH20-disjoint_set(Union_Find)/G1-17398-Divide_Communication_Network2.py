from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 9)


input = lambda: stdin.readline().rstrip()


def find(x: int) -> int:
    if parents[x] < 0:
        return x
    parents[x] = find(parents[x])
    return parents[x]


def union(x: int, y: int) -> None:
    x, y = find(x), find(y)
    if x == y:
        return
    parents[x] += parents[y]
    parents[y] = x


if __name__ == "__main__":
    N, M, Q = map(int, input().split())
    parents = [-1] * (N + 1)
    graph = [tuple(map(int, input().split())) for _ in range(M)]
    discxns = []
    checks = [True] * M
    for _ in range(Q):
        discxns.append(int(input()) - 1)
        checks[discxns[-1]] = False

    for i, (a, b) in enumerate(graph):
        if checks[i]:
            union(a, b)

    ans = 0
    visit = [False] * (N + 1)
    for i in range(Q - 1, -1, -1):
        a, b = find(graph[discxns[i]][0]), find(graph[discxns[i]][1])
        if a != b:
            ans += parents[a] * parents[b]
        union(a, b)

    print(ans)

"""
parents에는 -(그룹에 속한 노드 개수) 값을 저장
'음수 X 음수 = 양수' 이므로 ans에는 양수 비용이 저장됨

disconnect 되지 않은 간선에 대해 union -> disconnect된 간선을 역순으로 union하며 비용 계산
"""