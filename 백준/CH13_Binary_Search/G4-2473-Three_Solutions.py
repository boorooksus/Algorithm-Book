from sys import stdin, exit

if __name__ == "__main__":
    input = lambda: stdin.readline().rstrip()

    N = int(input())
    sols = list(map(int, input().split()))

    sols.sort()
    ans = []
    min_sum = int(3e9)
    for i in range(N - 2):
        if i > 0 and sols[i - 1] == sols[i]:
            continue

        left, right = i + 1, N - 1
        while left < right:
            temp = sols[i] + sols[left] + sols[right]

            if temp == 0:
                print("%d %d %d" % (sols[i], sols[left], sols[right]))
                exit(0)

            if abs(temp) < abs(min_sum):
                ans = [sols[i], sols[left], sols[right]]
                min_sum = temp

            if temp > 0:
                right -= 1
            else:
                left += 1

    print("%d %d %d" % (ans[0], ans[1], ans[2]))
