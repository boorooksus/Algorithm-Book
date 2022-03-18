from sys import stdin


def main():
    x = stdin.readline().rstrip()

    res = ''
    stack = []
    i = 0
    while i < len(x):
        if x[i] == '<':
            if stack:
                res += ''.join(stack[::-1])
                stack = []
            while x[i] != '>':
                res += x[i]
                i += 1
            res += x[i]

        elif x[i] == ' ':
            res += ''.join(stack[::-1])
            stack = []
            res += ' '
        else:
            stack.append(x[i])

        i += 1

    if stack:
        res += ''.join(stack[::-1])

    print(res)


if __name__ == "__main__":
    main()
