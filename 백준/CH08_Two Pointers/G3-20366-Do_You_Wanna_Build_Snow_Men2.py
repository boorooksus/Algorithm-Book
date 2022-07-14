from sys import stdin

input = lambda: stdin.readline().rstrip()

if __name__ == "__main__":
    N = int(input())
    H = list(map(int, input().split()))

    H.sort()
    ans = int(2e9)
    for i in range(N):
        for j in range(i + 3, N):
            left, right = i + 1, j - 1
            while left < right:
                temp = (H[i] + H[j]) - (H[left] + H[right])
                ans = min(abs(temp), ans)
                if temp < 0:
                    right -= 1
                else:
                    left += 1
    print(ans)

