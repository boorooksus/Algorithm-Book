from sys import stdin


res = set()


def dfs(orig, brackets, removes, cur):
    if cur == len(brackets):
        if not removes:
            return
        temp = ''
        for i, char in enumerate(orig):
            if i not in removes:
                temp += char
        res.add(temp)
        return

    dfs(orig, brackets, removes, cur + 1)
    dfs(orig, brackets, removes + brackets[cur], cur + 1)


def main():
    x = stdin.readline().rstrip()
    stack = []
    brackets = []

    for i, char in enumerate(x):
        if char == '(':
            stack.append(i)
        elif char == ')':
            brackets.append([stack.pop(), i])

    dfs(x, brackets, [], 0)
    print(*sorted(list(res)), sep='\n')


if __name__ == "__main__":
    main()
