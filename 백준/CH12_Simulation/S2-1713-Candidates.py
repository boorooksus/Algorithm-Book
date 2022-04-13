from sys import stdin


if __name__ == "__main__":
    def input():
        return stdin.readline().rstrip()

    n, m = (int(input()) for _ in range(2))
    nums = list(map(int, input().split()))

    recs = [0] * 101
    window = []
    order = [-1] * 101
    for i, num in enumerate(nums):
        if recs[num] != 0:
            recs[num] += 1
        elif n > 0:
            window.append(num)
            order[num] = i
            recs[num] += 1
            n -= 1
        else:
            out = min(window, key=lambda x: (recs[x], order[x]))
            window.remove(out)
            window.append(num)
            recs[out] = 0
            order[out] = -1
            order[num] = i
            recs[num] += 1

    print(*sorted(window))
