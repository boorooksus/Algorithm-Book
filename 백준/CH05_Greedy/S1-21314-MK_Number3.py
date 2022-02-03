from sys import stdin


def main():
    num = stdin.readline().rstrip()
    a, b = mk_number(num)
    print(a, b, sep='\n')


def mk_number(num: str) -> tuple[str, str]:
    mk_max = []
    mk_min = []
    for mword in num.split('K'):
        if mword:
            mk_max.append(str(5 * 10 ** (len(mword))))
            mk_min.append(str(10 ** (len(mword) - 1)))
        else:
            mk_max.append(str(5))
            mk_min.append('')

    max_val = ''.join(mk_max[:-1]) + '1' * (len(mk_max[-1]) - 1)
    min_val = '5'.join(mk_min)
    return max_val, min_val


if __name__ == "__main__":
    main()
