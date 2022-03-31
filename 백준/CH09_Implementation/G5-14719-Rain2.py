from sys import stdin


if __name__ == "__main__":
    def input():
        return stdin.readline().rstrip()

    h, w = map(int, input().split())
    heights = list(map(int, input().split()))

    ans = 0
    stack = []
    for i in range(w):
        while stack and heights[stack[-1]] < heights[i]:
            top = stack.pop()
            if not stack:
                break
            dist = i - stack[-1] - 1
            ans += (min(heights[i], heights[stack[-1]]) - heights[top]) * dist

        stack.append(i)

    print(ans)
