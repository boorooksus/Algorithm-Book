from sys import stdin
from collections import defaultdict


input = lambda: stdin.readline().rstrip()


def topology_sort():
    builts = [0] * (N + 1)

    for cmd, building in cmds:
        if cmd == 1:
            if indegs[building] > 0:
                return False
            if builts[building] == 0:
                for neighbor in graph[building]:
                    indegs[neighbor] -= 1
            builts[building] += 1
        else:
            if not builts[building]:
                return False
            builts[building] -= 1
            if builts[building] == 0:
                for neighbor in graph[building]:
                    indegs[neighbor] += 1
    return True


if __name__ == "__main__":
    N, M, K = map(int, input().split())
    graph = defaultdict(list)
    indegs = defaultdict(int)
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegs[b] += 1
    cmds = [tuple(map(int, input().split())) for _ in range(K)]
    print(['Lier!', 'King-God-Emperor'][topology_sort()])
