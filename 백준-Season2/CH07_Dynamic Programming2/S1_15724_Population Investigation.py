from sys import stdin

input = lambda: stdin.readline().rstrip()

if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = [[0] * (M + 1)] + \
          list([0] + list(map(int, input().split())) for _ in range(N))

    # 누적합 계산
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            arr[i][j] += arr[i - 1][j] + arr[i][j - 1] - arr[i - 1][j - 1]

    K = int(input())
    for _ in range(K):
        ay, ax, by, bx = map(int, input().split())
        print(arr[by][bx] - arr[ay - 1][bx] - arr[by][ax - 1] + arr[ay - 1][ax - 1])

"""
다이나믹 프로그래밍, 누적합
"""