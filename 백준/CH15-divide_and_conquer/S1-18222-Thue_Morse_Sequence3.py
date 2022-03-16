from sys import stdin


def thue_morse(idx: int) -> int:
    if idx == 0:
        return 0
    elif idx == 1:
        return 1
    elif idx % 2 == 1:
        return 1 - thue_morse(idx // 2)
    else:
        return thue_morse(idx // 2)


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
