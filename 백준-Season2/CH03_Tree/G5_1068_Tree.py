from sys import stdin
from collections import defaultdict, deque
input = lambda: stdin.readline().rstrip()


if __name__ == "__main__":
    N = int(input())
    parents = list(map(int, input().split()))
    removed = int(input())

    children = defaultdict(list)
    dq = deque()
    for i, parent in enumerate(parents):
        children[parent].append(i)
        if parent == -1 and i != removed:
            dq.append(i)

    ans = 0
    while dq:
        node = dq.popleft()
        cnt = 0
        for child in children[node]:
            if child != removed:
                dq.append(child)
                cnt += 1
        if cnt == 0:
            ans += 1

    print(ans)


"""
인덱스 0이 root가 아닐 수 있음 주의
"""