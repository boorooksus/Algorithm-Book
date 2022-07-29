from sys import stdin
from collections import defaultdict, deque
input = lambda: stdin.readline().rstrip()


def topology_sort():
    dq = deque()
    for person in people:
        if indgrs[person] == 0:
            dq.append(person)

    while dq:
        person = dq.popleft()
        for ancestor in ancestors[person]:
            indgrs[ancestor] -= 1
            if indgrs[ancestor] == 0:
                dq.append(ancestor)
                for descentant in descentants[ancestor]:
                    if not visit[descentant]:
                        children[ancestor].append(descentant)
                        visit[descentant] = True


if __name__ == "__main__":
    N = int(input())
    people = list(input().split())
    ancestors, descentants, indgrs = defaultdict(list), defaultdict(list), defaultdict(int)
    children, visit = defaultdict(list), defaultdict(bool)
    M = int(input())
    for _ in range(M):
        x, y = input().split()
        ancestors[x].append(y)
        descentants[y].append(x)
        indgrs[y] += 1

    topology_sort()

    root = []
    for person in people:
        if len(ancestors[person]) == 0:
            root.append(person)
    print(len(root))
    print(' '.join(sorted(root)))
    for person in sorted(ancestors.keys()):
        print(person, len(children[person]), ' '.join(sorted(children[person])), sep=' ')

