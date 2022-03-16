from sys import stdin
from math import log


def thue_morse(idx: int) -> int:
    if idx == 0:
        return 0

    x = int(log(idx, 2))

    val = 0
    while x > 0:
        if idx >= 2 ** x:
            val ^= 1
            idx %= 2 ** x
        x -= 1

    return [val, val ^ 1][idx == 1]


def main():
    k = int(stdin.readline())
    print(thue_morse(k - 1))


if __name__ == "__main__":
    main()


"""
0 01 0110 01101(0)01

01101(0)01  idx: 5, ord: 6
0(1)10      idx: 1, ord: 2
0(1)      idx: 1, ord: 2


"""
