from sys import stdin


if __name__ == "__main__":
    def input():
        return stdin.readline().rstrip()

    T = int(input())
    for _ in range(T):
        M = int(input())
        nums = []
        for _ in range(M // 10 + 1):
            nums += list(map(int, input().split()))

        ans, total = [], []
        for i, num in enumerate(nums):
            total.append(num)
            if i % 2 == 0:
                total.sort()
                ans.append(total[len(total) // 2])
        print(len(ans))
        for i in range(len(ans) // 10 + 1):
            print(*ans[10 * i:10 * (i + 1)], sep=' ')