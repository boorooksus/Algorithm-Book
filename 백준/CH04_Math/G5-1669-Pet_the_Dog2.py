"""
시간 초과
"""
from sys import stdin


if __name__ == "__main__":
    x, y = map(int, stdin.readline().rstrip().split())

    diff = y - x

    ans = 2 * (diff ** 0.5) - 1
    if float(int(ans)) == ans:
        print(int(ans))
        exit()

    ans = 2 * ((diff - 1) ** 0.5) - 1
    if float(int(ans)) == ans:
        print(int(ans) + 1)
        exit()

    ans = 2 * ((diff - 2) ** 0.5) - 1
    if float(int(ans)) == ans:
        print(int(ans) + 2)
        exit()

    ans = int((diff - 2) ** 0.5) - 1
    res = ans * (ans + 2)
    while True:
        if res == 2 * diff:
            print(int(ans))
            exit()
        elif res == 2 * (diff - 1):
            print(int(ans + 1))
            exit()
        elif res == 2 * (diff - 2):
            print(int(ans + 2))
            exit()
        ans += 1
        res = ans * (ans + 2)

"""
case 1
1 2 3 4 5 4 3 2 1 = 25 -> 9days

t = (n + 1) // 2
t ^ 2 = diff
(n + 1) ^ 2 = 4 * diff
n = 2 * sqrt(diff) - 1

=====
case 2
1 2 3 4 4 3 2 1 = 20 -> 8days

n // 2 * (n // 2 + 1) = diff
n + (n + 2) = 2 * diff

=====
case 3
1 2 1 1

=====
case 4
1 1 2 1 1
"""