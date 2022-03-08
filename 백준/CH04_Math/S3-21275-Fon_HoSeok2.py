from sys import stdin


# x진수 num을 10진수로 변환
def to_decimal(num: str, x: int, decimals: dict) -> int:
    res = 0
    for i, char in enumerate(num):
        res += (x ** (len(num) - i - 1)) * decimals[char]
    return res


def main():
    a, b = stdin.readline().split()

    decimals = {}
    for i in range(10):
        decimals[str(i)] = i
    for i in range(26):
        decimals[chr(i + 97)] = 10 + i

    a_nums, b_nums = [-1] * 37, [-1] * 37
    a_max, b_max = decimals[max(a)], decimals[max(b)]
    for i in range(a_max + 1, 37):
        a_nums[i] = to_decimal(a, i, decimals)
    for i in range(b_max + 1, 37):
        b_nums[i] = to_decimal(b, i, decimals)

    res = []
    for i in range(a_max + 1, 37):
        for j in range(b_max + 1, 37):
            if i == j:
                continue
            if a_nums[i] == b_nums[j]:
                res.append((a_nums[i], i, j))

    if len(res) > 1:
        print('Multiple')
    elif not res:
        print('Impossible')
    else:
        print(*res[0], sep=' ')


if __name__ == "__main__":
    main()
