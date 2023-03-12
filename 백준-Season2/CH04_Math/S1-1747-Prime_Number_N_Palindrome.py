from sys import stdin


def is_prime(x: int) -> bool:
    if x == 2 or x == 3:
        return True

    if x < 2 or x % 2 == 0:
        return False
    for i in range(3, int(x ** 0.5) + 2, 2):
        if x % i == 0:
            return False
    return True


def is_palindrome(x: int) -> bool:
    return str(x) == str(x)[::-1]


if __name__ == "__main__":
    N = int(stdin.readline())

    while True:
        if is_palindrome(N) and is_prime(N):
            print(N)
            break
        N += 1
