"""
bisect 안 쓴 방식
"""
from sys import stdin


if __name__ == "__main__":
    input = lambda: stdin.readline().rstrip()

    N = int(input())
    students = list(map(int, input().split()))

    students.sort()
    ans = 0
    for i in range(N - 2):
        left, right = i + 1, N - 1
        goal = -students[i]
        mx_idx = N
        while left < right:
            temp = students[left] + students[right]
            if goal == temp:
                if students[left] == students[right]:
                    ans += right - left
                else:
                    if right < mx_idx:
                        mx_idx = right
                        while mx_idx >= 0 and students[mx_idx - 1] == students[right]:
                            mx_idx -= 1
                    ans += right - mx_idx + 1
                left += 1
            elif temp < goal:
                left += 1
            else:
                right -= 1

    print(ans)
