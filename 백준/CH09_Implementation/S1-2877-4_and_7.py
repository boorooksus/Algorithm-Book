from sys import stdin


def sol(i: int, j: int) -> str:
    if i == 0:
        return ['4', '7'][j == 1]

    if j < 2 ** i:
        return '4' + sol(i - 1, j)
    else:
        return '7' + sol(i - 1, j % 2 ** i)


if __name__ == "__main__":
    K = int(stdin.readline().rstrip()) - 1

    n, i = 0, 0
    while n <= K:
        i += 1
        n += 2 ** i

    n -= 2 ** i
    i -= 1
    j = K - n

    print(sol(i, j))


"""
i군 j항

4 7
44 47 74 77
444 447 474 477 744 747 774 777 

"""