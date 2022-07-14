"""
prefix sum + two pointer
"""
from sys import stdin
input = lambda: stdin.readline().rstrip()


if __name__ == "__main__":
    N = int(input())
    dists = list(int(input()) for _ in range(N))

    # 거리 리스트 두 개를 이어 붙인 리스트의 prefix sum
    ps = [0] * (2 * N + 1)
    for i in range(2 * N):
        ps[i + 1] = ps[i] + dists[i % N]

    total = sum(dists)  # 전체 길이
    ans, left = 0, 0
    for right in range(2 * N):
        dist = ps[right] - ps[left]
        # 시계 방향 거리가 반시계 방향 거리보다 크면 거리를 줄임
        while dist > total - dist:
            left += 1
            dist = ps[right] - ps[left]
        # 최대 거리인지 확인
        ans = max(dist, ans)
    print(ans)
