from sys import stdin
input = lambda: stdin.readline().rstrip()


INF = int(3e9)


if __name__ == "__main__":
    N = int(input())
    solutions = list(map(int, input().split()))

    solutions.sort()
    val, res = INF, []
    left, right = 0, N - 1
    while left < right:
        temp = solutions[left] + solutions[right]

        if abs(temp) < val:
            val = abs(temp)
            res = [solutions[left], solutions[right]]

        left_move = abs(solutions[left + 1] + solutions[right])
        right_move = abs(solutions[left] + solutions[right - 1])
        if left_move < right_move:
            left += 1
        elif left_move > right_move:
            right -= 1
        else:
            left += 1
            right -= 1

    print(*res)

"""
5
-1 -2 -3 -4 -5

3
1 2 3

2
1000000000 1000000000

8
-100 -99 99 0 1 2 3 4 5

8
-1000000 -99 99 100 101 102 103 104 105

4
-100 -2 -1 10

7
-99 -2 -1 1 98 100 101

3
999999998 999999999 1000000000

10
-5 -5 -5 1 1 10 10 10 10 10

4
-3 -2 -1 2
"""