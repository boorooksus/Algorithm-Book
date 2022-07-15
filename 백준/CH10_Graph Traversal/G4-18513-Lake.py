from sys import stdin
from collections import deque, defaultdict
input = lambda: stdin.readline().rstrip()


def bfs(cnt: int) -> int:
    move = [1, -1]
    dq = deque()
    visit = defaultdict(bool)
    for lake in lakes:
        dq.append((0, lake))
        visit[lake] = True

    res = 0
    while dq:
        dist, node = dq.popleft()
        for i in range(2):
            next = node + move[i]
            if not visit[next]:
                dq.append((dist + 1, next))
                visit[next] = True
                res += dist + 1
                cnt -= 1
                if not cnt:
                    return res
    return res


if __name__ == "__main__":
    N, K = map(int, input().split())
    lakes = list(map(int, input().split()))

    print(bfs(K))
