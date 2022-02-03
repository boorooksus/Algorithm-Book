from sys import stdin


def main():
    num = stdin.readline().rstrip()
    a, b = mk_number(num)
    print(a, b, sep='\n')


def mk_number(num: str) -> tuple[str, str]:
    max_val, min_val = '', ''
    cnt = 0
    i = 0
    while True:
        while i < len(num) and num[i] == 'M':
            cnt += 1
            i += 1

        if i >= len(num):
            break

        max_val += str(int(5 * 10 ** cnt))
        if cnt > 0:
            min_val += str(int(10 ** (cnt - 1)))
        min_val += '5'

        cnt = 0
        i += 1

    if cnt > 0:
        max_val += '1' * cnt
        min_val += str(int(10 ** (cnt - 1)))

    return max_val, min_val


if __name__ == "__main__":
    main()
