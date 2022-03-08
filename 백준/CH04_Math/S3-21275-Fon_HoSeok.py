from sys import stdin


# x진수 num을 10진수로 변환
def to_decimal(num: str, x: int) -> int:
    cur, res = 0, 0
    for i in range(len(num)):
        if num[i].isdigit():
            cur = int(num[i])
        else:
            cur = ord(num[i]) - 97 + 10

        # 한 자리의 값이 x진수에서 나올 수 없는 수이면 -1 리턴
        if cur >= x:
            return -1

        res += (x ** (len(num) - i - 1)) * cur
    return res


def main():
    a, b = stdin.readline().split()

    a_decimals, b_decimals = [-1, -1], [-1, -1]
    for i in range(2, 37):
        a_decimals.append(to_decimal(a, i))
        b_decimals.append(to_decimal(b, i))

    res = []
    for i in range(2, 37):
        for j in range(2, 37):
            if i == j:
                continue
            if a_decimals[i] != -1 and a_decimals[i] == b_decimals[j]:
                res.append((a_decimals[i], i, j))

    if len(res) > 1:
        print('Multiple')
    elif not res:
        print('Impossible')
    else:
        print(*res[0], sep=' ')


if __name__ == "__main__":
    main()
