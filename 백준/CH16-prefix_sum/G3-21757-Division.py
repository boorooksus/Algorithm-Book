from sys import stdin
from math import factorial


input = lambda: stdin.readline().rstrip()


if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(1, N):
        arr[i] += arr[i - 1]

    # temp = arr.count(0)
    # cnt = 0
    # if temp >= 4:
    #     cnt = factorial(temp) // (factorial(temp - 4) * factorial(4))

    cnt = 0
    for i in range(N - 3):
        # if arr[i] < 0:
        #     continue
        temp = 0
        for j in range(i + 1, N - 2):
            if arr[j] - arr[i] != arr[i]:
                continue
            for k in range(j + 1, N - 1):
                if arr[k] - arr[j] != arr[i]:
                    continue
                for l in range(k + 1, N):
                    if arr[l] - arr[k] != arr[i]:
                        continue
                    temp += 1
        if temp >= 4:
            cnt += factorial(temp) // (factorial(temp - 4) * factorial(4))

    print(cnt)
