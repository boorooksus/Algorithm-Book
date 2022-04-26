from sys import stdin
from math import sqrt


def is_prime(num: int) -> bool:
    if num == 0 or num == 1:
        return False

    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True


if __name__ == "__main__":
    def input():
        return stdin.readline().rstrip()

    T = int(input())
    for _ in range(T):
        num = int(input())
        while True:
            if is_prime(num):
                print(num)
                break
            num += 1

