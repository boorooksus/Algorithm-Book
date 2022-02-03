from sys import stdin


primes = [True] * 1003002


def main():
    n = int(stdin.readline().rstrip())
    print(prime_palindrome(n))


def prime_palindrome(n: int) -> int:
    if n == 1 or n == 2:
        return 2

    primes[1] = False
    for i in range(2, 1003002):
        if not primes[i]:
            continue
        if i >= n and str(i)[::] == str(i)[::-1]:
            return i
        for j in range(2 * i, 1003002, i):
            primes[j] = False

    return -1


if __name__ == "__main__":
    main()


"""
에라토스테네스의 체 이용
속도 더 빠름
"""