from sys import stdin


def cal(line: str) -> int:
    table = {'(': ')', '[': ']'}
    score = {'(': 2, '[': 3}
    stack = []
    res = 1
    prev = ''
    for bracket in line:
        if bracket in '([':
            stack.append(bracket)
        else:
            if not stack or bracket != table[stack[-1]]:
                return 0

            pair = stack.pop()

            if not prev or prev in '([':
                res *= score[pair]
            else:
                res += score[pair]
        prev = bracket

    return res if not stack else 0


def main():
    line = stdin.readline().strip()
    print(cal(line))


if __name__ == "__main__":
    main()
