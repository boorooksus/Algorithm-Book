from sys import stdin
from bisect import bisect_left


if __name__ == "__main__":
    input = lambda: stdin.readline().rstrip()

    N = int(input())
    students = list(map(int, input().split()))

    students.sort()
    ans = 0
    for i in range(N - 2):
        left, right = i + 1, N - 1
        goal = -students[i]
        while left < right:
            temp = students[left] + students[right]
            if goal == temp:
                if students[left] == students[right]:
                    ans += right - left
                else:
                    idx = bisect_left(students, students[right], left, right)
                    ans += right - idx + 1
                left += 1
            elif temp < goal:
                left += 1
            else:
                right -= 1

    print(ans)
