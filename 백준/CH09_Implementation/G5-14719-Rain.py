from sys import stdin


if __name__ == "__main__":
    def input():
        return stdin.readline().rstrip()

    h, w = map(int, input().split())
    heights = list(map(int, input().split()))

    ans = 0
    left, right = 0, w - 1
    left_max, right_max = 0, 0
    while left < right:
        left_max = max(heights[left], left_max)
        right_max = max(heights[right], right_max)
        if left_max < right_max:
            ans += left_max - heights[left]
            left += 1
        else:
            ans += right_max - heights[right]
            right -= 1

    print(ans)
