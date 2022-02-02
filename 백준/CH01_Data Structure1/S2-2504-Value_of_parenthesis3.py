from sys import stdin


def cal(line: str) -> int:
    table = {'(': ')', '[': ']'}
    value = {'(': 2, '[': 3}
    stack = []
    res = 0

    for i, bracket in enumerate(line):
        if bracket in '([':
            stack.append(bracket)
        else:
            if not stack:
                return 0
            temp = 0
            while stack:
                top = stack.pop()
                if top.isdigit():
                    temp += int(top)
                elif bracket == table[top]:
                    if temp == 0:
                        stack.append(str(value[top]))
                    else:
                        stack.append(str(temp * value[top]))
                    break
                else:
                    return 0

    for i in stack:
        if i in '([':
            return 0
        else:
            res += int(i)

    return res


def main():
    line = stdin.readline().strip()
    print(cal(line))


if __name__ == "__main__":
    main()
