from sys import stdin


MAX = 1003001  # 1_000_000 보다 크거나 같고 소수이면서 팰린드롬인 가장 작은 수


def runner(x: int) -> int:
    if x < 2:
        return 2

    primes = [True] * (MAX + 1)

    for i in range(2, MAX + 1):
        if not primes[i]:
            continue

        if i >= x and str(i)[::] == str(i)[::-1]:
            return i

        for j in range(i * 2, MAX + 1, i):
            primes[j] = False


if __name__ == "__main__":
    N = int(stdin.readline())
    print(runner(N))


"""
에라토스테네스의 체를 이용한 소수 판별
속도  빠름
"""