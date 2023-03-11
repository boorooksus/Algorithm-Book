from sys import stdin
input = lambda: stdin.readline().rstrip()


if __name__ == "__main__":
    x = list(input())

    table = {')': '(', ']': '['}
    score = {')': 2, ']': 3}

    stack = []
    for bkt in x:
        if bkt in ['(', '[']:
            stack.append(bkt)
        else:
            if not stack:
                    print(0)
                    break

            temp = score[bkt]
            while stack and stack[-1] not in ['(', '[']:
                    temp *= stack.pop()
            if not stack or stack[-1] != table[bkt]:
                print(0)
                break
            stack.pop()
            while stack and stack[-1] not in ['(', '[']:
                try:
                    temp += stack.pop()
                except:
                    print(0)
                    exit(0)
            stack.append(temp)

    else:
        try:
            print(sum(stack))
        except:
            print(0)

