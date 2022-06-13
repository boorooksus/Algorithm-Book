"""
이진탐색
틀림
"""

from sys import stdin


input = lambda: stdin.readline().rstrip()
INF = 50002


if __name__ == "__main__":
    n, T = map(int, input().split())
    holds = [[0, 0]] + sorted(list(list(map(int, input().split())) for _ in range(n)), key=lambda crd: (crd[0] + crd[1], crd[0]))

    ans = INF
    left, right = 1, n - 1
    while left <= right:
        mid = left + (right - left) // 2
        visit = [False] * (n + 1)
        idx, cnt = 0, 0
        while holds[idx][1] < T:
            for nxt in range(idx + mid, idx - mid - 1, -1):
                if nxt < n + 1 and visit[nxt]:
                    continue
                if nxt < n + 1 and abs(holds[nxt][0] - holds[idx][0]) <= 2 and abs(holds[nxt][1] - holds[idx][1]) <= 2:
                    idx = nxt
                    cnt += 1
                    visit[nxt] = True
                    break
            else:
                right = mid - 1
                break
        else:
            ans = cnt
            left = mid + 1

    print([ans, -1][ans == INF])

