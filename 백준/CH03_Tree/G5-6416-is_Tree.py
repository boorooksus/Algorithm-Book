from sys import stdin
from collections import defaultdict, deque


def main():
    def input():
        return stdin.readline().rstrip()

    graph = defaultdict(list)
    indegree = defaultdict(int)
    nodes = set()
    cur = 1
    edge = 0
    while True:
        nums = list(map(int, input().split()))
        if len(nums) > 1 and nums[-1] < 0 and nums[-2] < 0:
            break

        for i in range(0, len(nums), 2):
            graph[nums[i]].append(nums[i + 1])
            indegree[nums[i + 1]] += 1
            nodes.add(nums[i])
            nodes.add(nums[i + 1])
            edge += 1

        if graph[0]:
            graph.pop(0)
            indegree[0] = 0
            nodes.remove(0)
            edge -= 1
            if is_tree(graph, indegree, nodes, edge):
                print('Case %d is a tree.' % cur)
            else:
                print('Case %d is not a tree.' % cur)
            graph.clear()
            indegree.clear()
            cur += 1
            edge = 0


def is_tree(graph, indegree, nodes, edge) -> bool:
    # if edge == 0:
    #     return True
    if len(nodes) != edge + 1:
        return False

    dq = deque()
    for node in nodes:
        if node != 0 and indegree[node] == 0:
            dq.append(node)
        if indegree[node] > 1:
            return False

    if len(dq) != 1:
        return False

    # for i in range(len(graph.keys())):
    #     if not dq:
    #         return False
    #
    #     node = dq.popleft()
    #     for neighbor in graph[node]:
    #         indegree[neighbor] -= 1
    #
    #         dq.append(neighbor)

    return True


if __name__ == "__main__":
    main()
