from sys import stdin


def cal(line: str) -> int:
    table = {'(': ')', '[': ']'}
    value = {'(': 2, '[': 3}
    stack = []
    res = 0
    temp = 1

    for i, bracket in enumerate(line):
        if bracket in '([':
            stack.append(bracket)
            temp *= value[bracket]
        else:
            if not stack or bracket != table[stack[-1]]:
                return 0
            if i > 0 and line[i - 1] == stack[-1]:
                res += temp
            temp //= value[stack.pop()]

    return res if not stack else 0


def main():
    line = stdin.readline().strip()
    print(cal(line))


if __name__ == "__main__":
    main()
