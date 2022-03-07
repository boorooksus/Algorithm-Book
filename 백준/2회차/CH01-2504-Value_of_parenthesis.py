from sys import stdin


def main():
    x = stdin.readline().rstrip()

    table = {')': '(', ']': '['}
    score = {')': 2, ']': 3}
    stack = []
    for i, char in enumerate(x):
        if char in "([":
            stack.append(char)
        elif not stack:
            print(0)
            return
        else:
            temp = 0
            cur = stack.pop()
            while stack and str(cur).isdigit():
                temp += cur
                cur = stack.pop()
            if cur != table[char]:
                print(0)
                return
            if temp > 0:
                temp *= score[char]
            else:
                temp = score[char]
            stack.append(temp)

    res = 0
    for num in stack:
        if not str(num).isdigit():
            print(0)
            return
        res += num
    print(res)


if __name__ == "__main__":
    main()
