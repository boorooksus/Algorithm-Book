from sys import stdin, maxsize


res = [maxsize, -maxsize]


def count_odds(x: str) -> int:
    cnt = 0
    for char in x:
        if char in '13579':
            cnt += 1
    return cnt


def cal(x: str, cur: int) -> None:
    if len(x) == 1:
        res[0] = min(count_odds(x) + cur, res[0])
        res[1] = max(count_odds(x) + cur, res[1])
        return

    elif len(x) == 2:
        cal(str(int(x[0]) + int(x[1])), cur + count_odds(x))

    else:
        odds = count_odds(x)
        for i in range(1, len(x) - 1):
            for j in range(i + 1, len(x)):
                cal(str(int(x[:i]) + int(x[i:j]) + int(x[j:])), cur + odds)


def main():
    x = stdin.readline().rstrip()
    cal(x, 0)
    print(*res, sep=' ')


if __name__ == "__main__":
    main()
