from sys import stdin
from math import sqrt


def main():
    n = int(stdin.readline().rstrip())
    print(prime_palindrome(n))


def prime_palindrome(n: int) -> int:
    if n == 1 or n == 2:
        return 2

    res = n if n % 2 == 1 else n + 1

    while True:
        if check(res):
            return res
        res += 2


def check(x: int) -> bool:
    for i in range(3, int(sqrt(x)) + 1, 2):
        if x % i == 0:
            return False

    return str(x)[::] == str(x)[::-1]


if __name__ == "__main__":
    main()
