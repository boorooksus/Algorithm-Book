from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 9)


def main():
    num = stdin.readline().rstrip()
    a, b = mk_number(num)
    print(a, b, end='\n')


def mk_number(num: str) -> tuple[str, str]:
    if not num:
        return '', ''

    if len(num) == 1:
        return str(mk2int(num)), str(mk2int(num))

    res = ('0' * len(num), '5' * len(num))  # (max value, min value)
    for i in range(1, len(num) + 1):
        prefix = str(mk2int(num[:i]))
        if prefix == '-1':
            continue
        a, b = mk_number(num[i:])

        res = (max(prefix + a, res[0]),
               min(prefix + b, res[1]))

    return res


def mk2int(num: str) -> int:
    if 'K' in num:
        if num.index('K') != len(num) - 1:
            return -1
        return 5 * 10 ** (len(num) - 1)
    else:
        return 10 ** (len(num) - 1)


if __name__ == "__main__":
    main()


"""
시간 초과
"""