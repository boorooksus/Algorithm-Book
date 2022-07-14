from sys import stdin

input = lambda: stdin.readline().rstrip()

if __name__ == "__main__":
    N = int(input())
    H = list(map(int, input().split()))

    H.sort()
    diff = sorted(list((H[i + 1] - H[i], i, i + 1) for i in range(N - 1)))
    left, right = 0, 1
    while diff[left][1] == diff[right][1] or \
            diff[left][1] == diff[right][2] or \
            diff[left][2] == diff[right][1] or \
            diff[left][2] == diff[right][2]:
        right += 1
    print(diff[left][0] + diff[right][0])
