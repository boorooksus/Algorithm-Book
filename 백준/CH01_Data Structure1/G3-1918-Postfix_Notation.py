from sys import stdin


if __name__ == "__main__":
    x = stdin.readline().rstrip()

    stack = []
    ans = ''
    for i in x:
        if i.isalpha():
            ans += i
        else:
            if i == '(':
                stack.append(i)
            elif i in "*/":
                while stack and stack[-1] in "*/":
                    ans += stack.pop()
                stack.append(i)
            elif i in "+-":
                while stack and stack[-1] in "*/+-":
                    ans += stack.pop()
                stack.append(i)
            elif i == ')':
                while stack and stack[-1] != "(":
                    ans += stack.pop()
                stack.pop()

    while stack:
        ans += stack.pop()

    print(ans)
